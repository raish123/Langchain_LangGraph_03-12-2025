import os,sys
import logging
from pathlib import Path
import datetime

#defining the directory where all logs get save 
log_dir = Path(r"MyProject\logs")

#now checking directory exist or not
if not os.path.exists(path=log_dir):
    os.makedirs(name=log_dir,exist_ok=True)


timestamp = datetime.datetime.now().strftime(format="%Y_%m_%d_%H_%M_%S")

log_filename =f"ai_logs_{timestamp}.log"
full_path_log = os.path.join(log_dir, log_filename)

format = '[%(asctime)s]-%(filename)s-%(levelname)s -%(message)s'

 
#now creating basicConfig class from logging module.
logging.basicConfig(
    format=format,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(full_path_log,mode="a",encoding="utf-8"),
        logging.StreamHandler(sys.stdout) #this line show/print log on terminal
    ],
    force=True 
    
)


# Get a logger instance
logger = logging.getLogger(name="ai_logs")
logger.setLevel(logging.INFO)
logger.propagate = True   # <--- this ensures logger uses basicConfig handlers
