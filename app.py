from src.MLproject.logger import logging
from src.MLproject.exception import CustomException
from src.MLproject.components.data_ingestion import DataIngestion
from src.MLproject.components.data_ingestion import DataIngestionConfig
from src.MLproject.components.data_transformation import DataTransformationConfig,DataTransformation
import sys

if __name__ == "__main__":
    logging.info("The execution has started")


    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion() 
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestions() 

        #DataTransformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)