from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidationConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logger.info("Initiating data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logger.info("Data ingestion completed")
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logger.info("Initiating data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logger.info("Data validation completed")
        print(data_validation_artifact)

        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logger.info("Initiating data transformation")
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logger.info("Data transformation completed")
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
