from steps.data_ingestion_step import data_ingestion_step
from steps.metadata_exploration_step import metadata_exploration_step
from steps.missing_values_step import missing_values_step
def run_pipeline():
    
    print("Running EDA pipeline...")

    print("Data ingestion commenced")
    data_ingestion_step()
    print("Data ingestion completed")


    print("Metadata exploration commenced")
    metadata_exploration_step()
    print("Metadata exploration completed")

    print("Missing value analysis commenced")