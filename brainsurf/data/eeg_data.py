import pandas as pd
import numpy as np
from scipy.signal import welch
class EEGData:
    def __init__(self, sampling_frequency=None, signal_columns=None, **kwargs):
        self.sampling_frequency = sampling_frequency
        self.signal_columns = signal_columns or []
        self.data = pd.DataFrame(kwargs)

    def __len__(self):
        return len(self.data)
    def drop_columns(self, columns):
        """
        Drop specified columns from the EEGData object.

        Parameters:
            columns (str or list): The column(s) to drop.

        Returns:
            None
        """
        if isinstance(columns, str):
            columns = [columns]  # Convert single column name to a list

        existing_columns = list(self.data.columns)
        columns_to_drop = [col for col in columns if col in existing_columns]

        if columns_to_drop:
            self.data.drop(columns=columns_to_drop, inplace=True)
        else:
            print("Specified column(s) not found in the EEGData object.")
    def get_data(self):
        return self.data

    def data_length(self):
        length = 0
        for value in self.data.values():
            if isinstance(value, list):
                length = max(length, len(value))
            else:
                length = max(length, len(str(value)))
        return length

    def calculate_length(self, key=None):
        if key is None:
            # Calculate the length of all keys
            lengths = [len(str(value)) for value in self.data.values()]
            return max(lengths)
        else:
            # Calculate the length of a specific key
            if key in self.data:
                value = self.data[key]
                return len(str(value))
            else:
                raise KeyError(f"Key '{key}' does not exist in the EEGData object.")

    def keys(self):
        return self.data.keys()

    def set_data(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, pd.Series):
                value = value.to_frame()  # Convert Series to DataFrame
            self.data[key] = value
            
    def dropna(self):
        """
        Remove rows with missing values from the EEGData object.

        Returns:
            None
        """
        self.data.dropna(inplace=True)

    def summary(self, max_len=5):
        """
        Prints a summary of the EEGData object by displaying the first n_samples keys and their corresponding values.

        Parameters:
            n_samples (int): The number of key-value pairs to display. Default is 5.

        Returns:
            None
        """
        print(self.data.head(max_len))


    def add_data(self, key, value):
        self.data[key] = value

    def remove_data(self, key):
        del self.data[key]

    def __getitem__(self, key):
        return self.data[key]

    def get_values(self, key):
        """
        Get the values of a particular key from the EEGData object.

        Parameters:
            key (str): The key to retrieve the values for.

        Returns:
            The values associated with the key.
        """
        if key in self.keys():
            values = self.get_data()[key]
            return values
        else:
            raise KeyError(f"Key '{key}' does not exist in the EEGData object.")
        
    def extract_frequency_bands(self, fs=None, epoch_size=1000):
        if 'raw' not in self.data:
            raise ValueError("Required key 'raw' is missing in the EEGData object.")

        if fs is None:
            fs = self.sampling_frequency or 128

        numeric_raw = pd.to_numeric(self.data['raw'], errors='coerce')
        raw_data = numeric_raw.dropna().to_numpy()
        if len(raw_data) == 0:
            raise ValueError("Raw EEG data must contain numeric values.")

        epoch_samples = max(2, int(round(epoch_size)))
        bands = {
            'delta': (1, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 50),
        }

        for band, (low, high) in bands.items():
            if band in self.data:
                continue

            features = np.full(len(self.data), np.nan)
            clean_index = numeric_raw.notna().to_numpy().nonzero()[0]

            for start in range(0, len(raw_data), epoch_samples):
                stop = min(start + epoch_samples, len(raw_data))
                epoch = raw_data[start:stop]
                if len(epoch) < 2:
                    continue

                f, psd = welch(epoch, fs=fs, nperseg=min(256, len(epoch)))
                band_psd = psd[(f >= low) & (f <= high)]
                band_power = np.mean(band_psd) if band_psd.size else np.nan
                features[clean_index[start:stop]] = band_power

            self.data[band] = features




class EEGDataFactory:
    def create_eeg_data(self, input_file):
        if isinstance(input_file, pd.DataFrame):
            return self.create_tabular_eeg_data(input_file)

        input_path = str(input_file)
        extension = input_path.lower()
        #CSV
        if extension.endswith('.csv'):
            data = self.parse_csv(input_file)
            return self.create_tabular_eeg_data(data)
        #EDF
        elif extension.endswith('.edf'):
            # Parse EDF data
            data = self.parse_edf(input_file)
            channel_names = data['channel_names']
            raw_data = data['raw_data']
            return EEGData(channel_names=channel_names, raw_data=raw_data)
    
        elif extension.endswith('.mff'):
            import mne

            raw = mne.io.read_raw_egi(input_file)
            eeg_data = raw.get_data()
            time_points = raw.times
            baseline = pd.DataFrame(data=eeg_data.T, columns=raw.ch_names)
            baseline['sec'] = time_points
            return baseline
            # Create EEGData object with the extracted data           
        
        elif extension.endswith('.xlsx') or extension.endswith('.xls'):
            data = self.parse_xlsx(input_file)
            return self.create_tabular_eeg_data(data)
        else:
            raise ValueError("Invalid file format. Only CSV, Excel, EDF, and MFF files are supported.")

    def create_tabular_eeg_data(self, data):
        data = data.copy()
        data.columns = [column.strip() if isinstance(column, str) else column for column in data.columns]

        column_lookup = {self.normalize_column_name(column): column for column in data.columns}
        time_column = self.find_first_column(
            column_lookup,
            ['sec', 'secs', 'second', 'seconds', 'time', 'time_s', 'timestamp', 'timestamps', 't'],
        )
        signal_columns = self.find_signal_columns(data, column_lookup, time_column)
        sampling_frequency = self.estimate_sampling_frequency(data[time_column]) if time_column is not None else None

        eeg_kwargs = {}
        if time_column is not None:
            eeg_kwargs['sec'] = pd.to_numeric(data[time_column], errors='coerce')

        channel_frame = data[signal_columns].apply(pd.to_numeric, errors='coerce')
        if len(signal_columns) == 1:
            eeg_kwargs['raw'] = channel_frame[signal_columns[0]]
        else:
            eeg_kwargs['raw'] = channel_frame.mean(axis=1)
            for column in signal_columns:
                eeg_kwargs[column] = channel_frame[column]

        for band in ['alpha', 'beta', 'delta', 'theta', 'gamma']:
            band_column = column_lookup.get(band)
            if band_column is not None:
                eeg_kwargs[band] = pd.to_numeric(data[band_column], errors='coerce')

        eeg_data = EEGData(
            sampling_frequency=sampling_frequency,
            signal_columns=list(signal_columns),
            **eeg_kwargs,
        )
        eeg_data.extract_frequency_bands(fs=sampling_frequency)
        return eeg_data

    def find_signal_columns(self, data, column_lookup, time_column=None):
        primary_signal = self.find_first_column(
            column_lookup,
            ['eeg', 'raw', 'signal', 'value', 'amplitude', 'voltage', 'microvolts', 'uv'],
        )
        if primary_signal is not None:
            return [primary_signal]

        numeric_columns = list(data.select_dtypes(include=[np.number]).columns)
        excluded_columns = {time_column}
        excluded_columns.update(
            column_lookup[name]
            for name in [
                'alpha',
                'beta',
                'delta',
                'theta',
                'gamma',
                'id',
                'subject',
                'participant',
                'trial',
                'event',
                'label',
                'class',
                'target',
            ]
            if name in column_lookup
        )
        signal_columns = [column for column in numeric_columns if column not in excluded_columns]
        if signal_columns:
            return signal_columns

        raise ValueError(
            "Tabular EEG data must include an EEG/raw/signal column or at least one numeric EEG channel."
        )

    def find_first_column(self, column_lookup, names):
        for name in names:
            if name in column_lookup:
                return column_lookup[name]
        return None

    def normalize_column_name(self, column):
        return str(column).strip().lower().replace(' ', '_').replace('-', '_')

    def estimate_sampling_frequency(self, timestamps):
        timestamps = pd.to_numeric(timestamps, errors='coerce').dropna().to_numpy()
        if len(timestamps) < 2:
            return None

        time_diff = np.diff(timestamps)
        time_diff = time_diff[time_diff > 0]
        if len(time_diff) == 0:
            return None

        return 1 / np.nanmedian(time_diff)
    
    

    def parse_csv(self, input_file):
        data = pd.read_csv(input_file)
        return data

    def parse_edf(self, input_file):
        import pyedflib

        f = pyedflib.EdfReader(input_file)
        channel_names = f.getSignalLabels()
        raw_data = []
        for i in range(f.signals_in_file):
            raw_data.append(f.readSignal(i))
        f.close()
        data = {'channel_names': channel_names, 'raw_data': raw_data}
        return data
    
    def parse_xlsx(self, input_file):
        data = pd.read_excel(input_file)
        return data
    
