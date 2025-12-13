from dotenv import load_dotenv
import os,sys
from logger_config import logger
from exception import CustomException


try:
    logger.info(msg="Loading the environment Variable")
    load_dotenv()
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")

    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
    S3_PREFIX = os.getenv("S3_PREFIX")
    
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    INDEX_NAME = os.getenv("INDEX_NAME")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")

    logger.info(msg="Environment Variable successfully Loaded")

except Exception as e:
    raise CustomException(e,sys)