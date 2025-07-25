import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
def missing_values_step(df: pd.DataFrame) -> None:
    """
    This function will contain the logic to handle missing values in the dataset.
    It will identify columns with missing values and provide options for handling them.
    """
    
    print("Missing value analysis commenced")
    
    print("Identifying columns with missing values...",df.isnull().sum())
    
    # 🔹 MATRIX PLOT: Visual row-wise missing value distribution
    plt.figure(figsize=(10, 6))
    msno.matrix(df)
    plt.title("Missing Value Matrix")
    plt.show()

    # 🔹 HEATMAP PLOT: Correlation between missing values
    plt.figure(figsize=(10, 6))
    msno.heatmap(df)
    plt.title("Missing Value Correlation Heatmap")
    plt.show()