
import pandas as pd
import pyedflib

class EEGData:
    def __init__(self, **kwargs):
        self.data = {}
        for key, value in kwargs.items():
            self.data[key] = value
    def __len__(self):
        return len(self.data)
    def get_data(self):
        return self.data
    
    def keys(self):
        return self.data.keys()
    
    def set_data(self, **kwargs):
        self.data.update(kwargs)

    def summary(self, max_len):
            return {key: self.data[key][:max_len] for key in self.data}
        
    def head(self, n_samples=5):
        """
        Prints a summary of the EEGData object by displaying the first n_samples keys and their corresponding values.

        Parameters:
            n_samples (int): The number of key-value pairs to display. Default is 5.

        Returns:
            None
        """
        print("EEGData object summary:")
        data_dict = {key: value[:n_samples] for key, value in self.data.items()}
        df = pd.DataFrame(data_dict)
        print(df)



    def add_data(self, key, value):
        self.data[key] = value

    def remove_data(self, key):
        del self.data[key]

class EEGDataFactory:
    def create_eeg_data(self, input_file):
        if input_file.endswith('.csv'):
            data = self.parse_csv(input_file)
            print(data.columns)
            if 'sec' in data.columns and 'EEG' in data.columns and 'alpha' in data.columns and 'beta' in data.columns and 'delta' in data.columns and 'theta ' in data.columns:
                # CSV data with sec, alpha, beta, and gamma columns            
                return EEGData(sec=data['sec'], raw=data['EEG'], alpha=data['alpha'], beta=data['beta'], theta=data['theta '], delta =data['delta'])
            elif 'time' in data.columns:
                # CSV data with raw and time columns
                return EEGData(time=data['time'], raw=data['EEG'])
            else:
                # CSV data with only raw data
                return EEGData(raw=data['EEG'])
        elif input_file.endswith('.edf'):
            # Parse EDF data
            data = self.parse_edf(input_file)
            channel_names = data['channel_names']
            raw_data = data['raw_data']
            return EEGData(channel_names=channel_names, raw_data=raw_data)

    def parse_csv(self, input_file):
        # Parse CSV data into a Pandas DataFrame
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
    
    
# import pandas as pd
# import pyedflib

# class EEGData(pd.DataFrame):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def summary(self, max_len):
#         return self.iloc[:max_len]

#     def add_data(self, key, value):
#         self[key] = value

#     def remove_data(self, key):
#         del self[key]

#     def keys(self):
#         return self.columns.tolist()

#     def head(self, n=5):
#         return self.iloc[:n]


# class EEGDataFactory:
#     def create_eeg_data(self, input_file):
#         if input_file.endswith('.csv'):
#             data = self.parse_csv(input_file)
#             print(data.columns)
#             if 'sec' in data.columns and 'EEG' in data.columns and 'alpha' in data.columns and 'beta' in data.columns and 'delta' in data.columns and 'theta ' in data.columns:
#                 # CSV data with sec, alpha, beta, and gamma columns            
#                 return EEGData(sec=data['sec'], raw=data['EEG'], alpha=data['alpha'], beta=data['beta'], theta=data['theta '], delta =data['delta'])
#             elif 'sec' in data.columns:
#                 # CSV data with raw and time columns
#                 return EEGData(time=data['sec'], raw=data['EEG'])
#             else:
#                 # CSV data with only raw data
#                 return EEGData(raw=data['EEG'])
#         elif input_file.endswith('.edf'):
#             # Parse EDF data
#             data = self.parse_edf(input_file)
#             channel_names = data['channel_names']
#             raw_data = data['raw_data']
#             return EEGData(channel_names=channel_names, raw_data=raw_data)

#     def parse_csv(self, input_file):
#         # Parse CSV data into a Pandas DataFrame
#         data = pd.read_csv(input_file)
#         return data

#     def parse_edf(self, input_file):
#         f = pyedflib.EdfReader(input_file)
#         channel_names = f.getSignalLabels()
#         raw_data = []
#         for i in range(f.signals_in_file):
#             raw_data.append(f.readSignal(i))
#         f.close()
#         data = {'channel_names': channel_names, 'raw_data': raw_data}
#         return data
    
    

