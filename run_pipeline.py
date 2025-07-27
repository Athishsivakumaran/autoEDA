from steps.data_ingestion_step import data_ingestion_step
from steps.metadata_exploration_step import metadata_exploration_step
from steps.missing_values_step import missing_values_step
from steps.univariate_analysis import run_univariate_analysis
from steps.bivariate_analysis import run_bivariate_analysis
from steps.multivariate_analysis import run_multivariate_analysis
from steps.target_variable_analysis import run_target_variable_analysis


import pandas as pd
def run_pipeline():
    # file_path = "/Users/athish/EDA_explorer/data/archive.zip"  # Path to the ZIP file containing the dataset
    print("Running EDA pipeline...")

    print("Data ingestion commenced")
    # df = data_ingestion_step(file_path)
    print("Data ingestion completed")

    df = pd.read_csv("/Users/athish/EDA_explorer/extracted_data/AmesHousing.csv")
    print("Metadata exploration commenced")
    metadata_exploration_step(df)
    print("Metadata exploration completed")

    print("Missing value analysis commenced")
    missing_values_step(df)
    print("Missing value analysis completed")

    print("Univariate analysis commenced")
    run_univariate_analysis(df)
    print("Univariate analysis completed")

    print("Univariate analysis commenced")
    run_bivariate_analysis(df)
    print("Univariate analysis completed")

    print("Multivariate analysis commenced")
    run_multivariate_analysis(df)
    print("Multivariate analysis completed")

    print("Target variable analysis commenced")
    target_col = df.columns[-1]
    run_target_variable_analysis(df, target_col)
    print("Target variable analysis completed")