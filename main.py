from insurance.logger import logging
from insurance.exception import InsurancsException
import os,sys
from insurance.utils import get_collection_as_dataframe


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
        get_collection_as_dataframe(database_name="INSURANCE",collection_name="INSURANCE_PROJECT")
    except Exception as e:
        print(e)