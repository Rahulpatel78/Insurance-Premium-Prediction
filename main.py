from insurance.logger import logging
from insurance.exception import InsurancsException
import os,sys
from insurance.utils import get_collection_as_dataframe
from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity import config_entity
from insurance.components.data_ingestion import DataIngestion


#def test_logging_and_exception():
    #try:
        #logging.info("strating the test_logger_and_exception")
        #result = 3 / 10
        #print(result)
        #logging.info("ending point of the test_logger")
    #except Exception as e:
       # logging.debug(str(e))
       # raise InsurancsException(e, sys)

if __name__=="__main__":
    try:
        #test_logging_and_exception()
        #get_collection_as_dataframe(database_name="INSURANCE",collection_name="INSURANCE_PROJECT")
        TrainingPipelineConfig = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config=TrainingPipelineConfig)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
        data_ingestion_artifact = data_ingestion.intitate_data_ingestion()
    except Exception as e:
        print(e)