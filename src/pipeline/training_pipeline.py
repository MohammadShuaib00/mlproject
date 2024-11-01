from src.logger.logging import logging
from src.exception.exception import CustomException
import os, sys
from src.constant import training_pipeline
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.components.data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self):
        self.traning_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(
                training_pipeline_config=self.traning_pipeline_config
            )
            logging.info("Start data Ingestion")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(
                f"Data Ingestion completed and artifact: {data_ingestion_artifact}"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(str(e), sys.exc_info())
        
starting = TrainingPipeline()
