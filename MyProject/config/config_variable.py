from dotenv import load_dotenv
import os,sys
from logger_config import logger
from exception import CustomException


try:
    logger.info(msg="Loading the environment Variable")
    load_dotenv()
    logger.info(msg="Environment Variable successfully Loaded")

except Exception as e:
    raise CustomException(e,sys)