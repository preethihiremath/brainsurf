import streamlit as st
import brainsurf.preprocessing.filtering as filter
import numpy as np

import brainsurf.data.csv as csv_import


def main():
    # Configure Streamlit
    st.set_page_config(page_title='Brainsurf App', layout='wide')

    # Add title and description
    st.title('Brainsurf App')
    st.write('Welcome to the Brainsurf App!')

    # Add your app's functionality using Streamlit components
    # For example:
    # - Display inputs using st.sidebar or st.text_input, st.selectbox, etc.
    # - Perform computations or call functions based on user inputs
    # - Display results or visualizations using st.pyplot, st.table, etc.

    # Example: Load data and apply bandpass filter
    st.header('Data Loading and Filtering')
    st.subheader('Load EEG Data')
    file_path = st.text_input('Enter the file path:')
    adarsh_pre_med = None  # Initialize data variable

    if st.button('Load Data'):
        try:
            adarsh_pre_med = csv_import.convert_csv_to_eegdata(file_path)
            # data_summary = adarsh_pre_med.summary(300)
            st.success('Data loaded successfully!')
        except:
            st.error('Error loading data. Please check the file path.')

    st.subheader('Apply Bandpass Filter')
    low_freq = st.number_input('Enter the low-frequency cutoff:', min_value=0.0, max_value=100.0, value=1.0)
    high_freq = st.number_input('Enter the high-frequency cutoff:', min_value=0.0, max_value=100.0, value=30.0)
    sampling_freq = st.number_input('Enter the high-frequency cutoff:')


    if st.button('Apply Filter'):
        if adarsh_pre_med is not None:
            order = 4
            filtered_data = filter.butter_bandpass_filter(adarsh_pre_med['raw'], low_freq, high_freq, sampling_freq, order) 
            st.write(adarsh_pre_med)
            st.success('Filter applied successfully!')
        else:
            st.warning('Please load data before applying the filter.')

    # Example: Display statistics
    st.header('Statistics')
    if 'filtered_data' in locals():
        st.subheader('Data Statistics')
        st.write('Mean:', np.mean(filtered_data))
        st.write('Standard Deviation:', np.std(filtered_data))
        st.write('Minimum:', np.min(filtered_data))
        st.write('Maximum:', np.max(filtered_data))
    else:
        st.warning('Please load data and apply the filter before displaying statistics.')

if __name__ == '__main__':
    main()
