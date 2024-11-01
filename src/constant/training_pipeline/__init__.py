import os
import sys


# Base directory for artifacts
PIPELINE_NAME: str = "StudentPerformance"
ARTIFACT_DIR: str = "artifact"

# Define paths for data ingestion
DATA_INGESTION_DIR: str = "dataIngestion"
RAW_DATA_PATH: str = "raw.csv"
TRAIN_DATA_PATH: str = "train.csv"
TEST_DATA_PATH: str = "test.csv"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.20
