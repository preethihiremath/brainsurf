import pyabf
import pandas as pd

def convert_acq_to_csv(acq_file, csv_file):
    abf = pyabf.ABF(acq_file)
    df = pd.DataFrame(abf.data)
    return df
