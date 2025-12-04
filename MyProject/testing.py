from logger_config import logger
from exception import CustomException
import os,sys



try:
    logger.info("Testing logger...")  # Adding THIS
    a = 1/0
except Exception as e:
    logger.error("Error occurred")  # Adding THIS
    raise CustomException(e, sys)
