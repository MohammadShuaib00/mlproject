import os
import sys
from src.logger.logging import logging
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from src.constant import training_pipeline
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from src.entity.artifact_entity import DataIngestionArtifact
import pandas as pd


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(str(e), sys.exc_info())

    def split_data_as_train_and_test(self, dataframe: pd.DataFrame):
        try:
            logging.info("Performing train-test split on the dataframe")
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            train_set.to_csv(
                self.data_ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.test_data_path, index=False, header=True
            )
            logging.info("Exported train and test files successfully.")

        except Exception as e:
            raise CustomException(str(e), sys.exc_info())

    def get_initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Reading the data from local machine")

            # Ensure directory exists before saving files
            os.makedirs(
                os.path.dirname(self.data_ingestion_config.raw_data), exist_ok=True
            )

            # Read dataset
            df = pd.read_csv("data/stud.csv")
            print(f"The shape of the dataset: {df.shape}")

            # Save the raw data
            df.to_csv(self.data_ingestion_config.raw_data, index=False, header=True)

            # Perform train-test split and save the split datasets
            self.split_data_as_train_and_test(df)

            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path,
            )
            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(str(e), sys.exc_info())


# Correctly instantiate DataIngestionConfig
data_ingestion_config = DataIngestionConfig(
    training_pipeline_config=TrainingPipelineConfig()
)
obj = DataIngestion(data_ingestion_config=data_ingestion_config)
artifact = obj.get_initiate_data_ingestion()
print(f"Train file path: {artifact.trained_file_path}")
print(f"Test file path: {artifact.test_file_path}")
