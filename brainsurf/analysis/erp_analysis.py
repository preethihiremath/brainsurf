# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# def epoch_data(df, epoch_length, event_column, event_id, fs):
   
#     event_sample = (df[event_column] == event_id).astype(int).diff()
#     event_sample.iloc[0] = 0
#     event_sample = event_sample[event_sample == 1].index.values[0]
    
#     # Determine the number of samples in each epoch
#     epoch_samples = int(epoch_length * fs)
    
#     # Determine the number of epochs that can be extracted
#     n_epochs = int(np.floor((len(df) - event_sample) / epoch_samples))
    
#     # Epoch the data
#     epochs = []
#     for i in range(n_epochs):
#         epoch_start = event_sample + i * epoch_samples
#         epoch_end = epoch_start + epoch_samples
#         epoch_data = df.iloc[epoch_start:epoch_end, :-2].values
#         epochs.append(epoch_data)
        
#     return epochs

# def average_epochs(epochs):
    
#     avg_epoch = np.mean(epochs, axis=0)
#     return avg_epoch

# def plot_erp(avg_epoch, fs):  
#     time_axis = np.arange(avg_epoch.shape[0]) / fs
#     plt.plot(time_axis, avg_epoch)
#     plt.xlabel('Time (s)')
#     plt.ylabel('Amplitude (uV)')
#     plt.show()

# def extract_p300(avg_epoch, fs):
    
    
#     p300_peak_sample = np.argmax(avg_epoch)

#     p300_onset_sample = int(fs * 0.2)  # assume P300 onset is 200 ms after the event onset
    
#     # Find the sample corresponding to the end of the P300
#     p300_end_sample = int(fs * 0.6)  # assume P300 ends 600 ms after the event onset
    
#     # Extract the P300 component
#     p300 = avg_epoch[p300_onset_sample:p300_end_sample]
    
#     # Adjust the time axis to reflect the P300 component
#     time_axis = np.arange(len(p300)) / fs + p300_onset_sample / fs
    
#     return p300, time_axis


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def erp_analysis(data, event_column, event_id, tmin=-0.2, tmax=0.8):
    """
    Perform ERP analysis on the given data.

    Parameters
    ----------
    data : pandas DataFrame
        EEG data with channels as columns and time as index.
    event_column : str
        Column name indicating the onset of each stimulus or trial.
    event_id : int or list of int
        Event ID(s) to use for epoching the data.
    tmin : float, optional
        Start time of the epoch in seconds relative to the event onset.
    tmax : float, optional
        End time of the epoch in seconds relative to the event onset.

    Returns
    -------
    erp : pandas DataFrame
        Average ERP waveform for each channel.
    """
    # Convert the event column to a list
    events = data[event_column].tolist()

    # Find the index of each event in the data
    event_index = [0]
    for i in range(1, len(events)):
        if events[i] != events[i-1]:
            event_index.append(i)

    # Create epochs from the data
    epoch_data = []
    for idx in event_index:
        epoch = data.iloc[idx + int(tmin*1000):idx + int(tmax*1000) + 1, :]
        epoch_data.append(epoch.values)
    epoch_data = np.array(epoch_data)

    # Compute the average of the epochs to obtain the ERP waveform
    erp = pd.DataFrame(epoch_data.mean(axis=0), columns=data.columns)

    # Visualize the ERP waveform
    plt.figure()
    plt.plot(erp.index, erp.values)
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude (uV)')
    plt.title('ERP Waveform')
    plt.legend(erp.columns)

    # Extract ERP components of interest
    # ...

    return erp
