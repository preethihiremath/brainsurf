import pyedflib
import pandas as pd

def read_edf_to_dataframe(file_path):
    f = pyedflib.EdfReader(file_path)
    signal_labels = f.getSignalLabels()
    sample_rates = f.getSampleFrequencies()
    data = {}
    for i, label in enumerate(signal_labels):
        signal_data = f.readSignal(i)
        data[label] = signal_data
    
    df = pd.DataFrame(data)
    start_time = pd.Timestamp(f.getStartdatetime())
    end_time = start_time + pd.Timedelta(seconds=f.getFileDuration())
    time_index = pd.date_range(start=start_time, end=end_time, periods=len(df))
    df.index = time_index
    df = df.resample(pd.Timedelta(seconds=1/sample_rates[0])).mean()
    df.index.name = 'Time'
    f.close()
    
    return df
