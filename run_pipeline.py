from steps.data_ingestion_step import data_ingestion_step
from steps.metadata_exploration_step import metadata_exploration_step
from steps.missing_values_step import missing_values_step
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