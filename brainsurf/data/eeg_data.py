import pandas as pd
import pyedflib
import h5py 
import numpy as np

class EEGData:
    def __init__(self, **kwargs):
        self.data = pd.DataFrame(kwargs)

    def __len__(self):
        return len(self.data)

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


class EEGDataFactory:
    def create_eeg_data(self, input_file):

        #CSV
        if input_file.endswith('.csv'):
            data = self.parse_csv(input_file)
            if 'sec' in data.columns and 'EEG' in data.columns and 'alpha' in data.columns and 'beta' in data.columns and 'delta' in data.columns and 'theta ' in data.columns:
                # CSV data with sec, alpha, beta,  delta and theta columns            
                return EEGData(sec=data['sec'], raw=data['EEG'], alpha=data['alpha'], beta=data['beta'], theta=data['theta '], delta =data['delta'])
            elif 'sec' in data.columns:
                # CSV data with raw and sec columns
                return EEGData(sec=data['sec'], raw=data['EEG'])
            else:
                # CSV data with only raw data
                return EEGData(raw=data['EEG'])
        #EDF
        elif input_file.endswith('.edf'):
            # Parse EDF data
            data = self.parse_edf(input_file)
            channel_names = data['channel_names']
            raw_data = data['raw_data']
            return EEGData(channel_names=channel_names, raw_data=raw_data)
    
        elif input_file.endswith('.mff'):
            data = self.parse_mff(input_file)
           
            if 'sec' in data.columns and 'EEG' in data.columns and 'alpha' in data.columns and 'beta' in data.columns and 'delta' in data.columns and 'theta ' in data.columns:
                    # CSV data with sec, alpha, beta, and gamma columns            
                    return EEGData(sec=data['sec'], raw=data['EEG'], alpha=data['alpha'], beta=data['beta'], theta=data['theta '], delta =data['delta'])
            elif 'sec' in data.columns:
                    # CSV data with raw and time columns
                    return EEGData(time=data['sec'], raw=data['EEG'])
            elif 'EEG' in data.col:
                    # CSV data with only raw data
                    return EEGData(raw=data['EEG'])
            else:
                return EEGData(sec=data['time'], raw=data['EEG'], channel_names=channel_names)
            # Create EEGData object with the extracted data           
        
        elif input_file.endswith('.xlsx'):
            data = self.parse_xlsx(input_file)
            # Extract relevant information from the XLSX data
            if 'sec' in data.columns and 'EEG' in data.columns and 'alpha' in data.columns and 'beta' in data.columns and 'delta' in data.columns and 'theta ' in data.columns:
                    # CSV data with sec, alpha, beta, and gamma columns            
                    return EEGData(sec=data['sec'], raw=data['EEG'], alpha=data['alpha'], beta=data['beta'], theta=data['theta '], delta =data['delta'])
            elif 'sec' in data.columns:
                    # CSV data with raw and time columns
                    return EEGData(sec=data['sec'], raw=data['EEG'])
            else:
                    # CSV data with only raw data
                    return EEGData(raw=data['EEG'])
        else:
            raise ValueError("Invalid file format. Only CSV, EDF, MFF, and XLSX files are supported.")
 
  
    def parse_mff(self, input_file):
        # Implement your MFF file parsing logic here
        with h5py.File(input_file, 'r') as f:
            sec = f['/path/to/timestamps'][()]  # Replace '/path/to/timestamps' with the actual dataset path
            eeg_signals = f['/path/to/eeg_signals'][()]  # Replace '/path/to/eeg_signals' with the actual dataset path
            channel_names = f['/path/to/channel_names'][()]  # Replace '/path/to/channel_names' with the actual dataset path
        
        data = {'sec': sec, 'eeg_signals': eeg_signals, 'channel_names': channel_names}
        return data

    def parse_csv(self, input_file):
        data = pd.read_csv(input_file)
        return data

    def parse_edf(self, input_file):
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
    