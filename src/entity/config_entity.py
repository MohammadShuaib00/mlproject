import os
import sys
from src.constant import training_pipeline
from datetime import datetime

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR
        )
        self.raw_data: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.RAW_DATA_PATH
        )
        self.train_data_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.TRAIN_DATA_PATH
        )
        self.test_data_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.TEST_DATA_PATH
        )
        self.train_test_split_ratio: float = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        )
