import pandas as pd


def metadata_exploration_step(df: pd.DataFrame) -> None:
    """
    This function will contain the logic to explore metadata of the dataset.
    It will include operations like checking for missing values, data types,
    and basic statistics of the dataset.
    """
    
    
    print("Shape of the DataFrame:", df.shape)
    print("Columns in the DataFrame:", df.columns.tolist())
    print("Data types of each column:\n", df.dtypes)
    print("Basic statistics of the DataFrame:\n", df.describe())
    print("Information",df.info())
    print("head of the DataFrame:\n", df.head())
    print("tail of the DataFrame:\n", df.tail())    
    print("sample of the DataFrame:\n", df.sample(10))
    print("Unique values in each column:",df.nunique())
    print("Duplicate rows in the DataFrame:", df.duplicated().sum())

    return
    
