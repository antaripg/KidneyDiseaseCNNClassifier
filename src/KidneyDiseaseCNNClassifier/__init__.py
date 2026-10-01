import os
import sys
import logging

# Logging String 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

# Logging directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO, # Which logging level to use
    # Which Format to use for logging messages
    format=logging_str,
    # Handlers to write logs to both file and console
    handlers=[
        logging.FileHandler(log_filepath), # Log file handler
        logging.StreamHandler(sys.stdout) # Log to console
    ]
)
# Get the logger instance for the module
logger = logging.getLogger("KidneyDiseaseCNNClassifier")


