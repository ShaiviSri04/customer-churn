import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load churn dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    df = pd.read_csv(file_path)
    return df
