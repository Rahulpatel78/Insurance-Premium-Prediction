import os, sys
from insurance.exception import InsurancsException
from insurance.logger import logging
from datetime import datetime



class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise InsurancsException(e, sys)

class DataIngestionConfig:
    pass



class DataValidation:
    pass