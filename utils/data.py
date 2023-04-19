import pandas as pd

def get_columns(dataset, columns):
    """
    Get specific columns from the dataset.
    
    Parameters:
    -----------
    dataset : str or pandas.DataFrame
        The dataset to extract columns from. It can be either a path to a CSV file or a pandas DataFrame.
    columns : list
        A list of column names to extract from the dataset.
        
    Returns:
    --------
    pandas.DataFrame
        A DataFrame with the selected columns.
    """
    if isinstance(dataset, str):
        # If dataset is a string, assume it's a path to a CSV file
        df = pd.read_csv(dataset)
    elif isinstance(dataset, pd.DataFrame):
        # If dataset is a DataFrame, use it directly
        df = dataset
    else:
        #Update to handle more types directly
        raise TypeError("dataset must be either a path to a CSV file or a pandas DataFrame.")
    
    # Check if all columns are in the dataset
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the dataset.")
    return df[columns]
    
