import logging
from datetime import datetime
import os


LOG_DIR = "insurance_log"

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR , exist_ok = True)

LOG_FILE_PATH = os.path.join(LOG_DIR , LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode= 'w',
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)

