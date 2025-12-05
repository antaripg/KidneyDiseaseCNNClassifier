import os
from pathlib import Path
import logging


# Logging String
logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s] %(levelname)s : %(message)s',)
logger = logging.getLogger(__name__)

projet_name = "KidneyDiseaseCNNClassifier"

# List of  files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projet_name}/__init__.py",
    f"src/{projet_name}/components/__init__.py",
    f"src/{projet_name}/utils/__init__.py",
    f"src/{projet_name}/config/__init__.py",
    f"src/{projet_name}/config/configuration.py",
    f"src/{projet_name}/pipeline/__init__.py",
    f"src/{projet_name}/entity/__init__.py",
    f"src/{projet_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# Create the files
for filepath in list_of_files:
    filepath = Path(filepath) # Detects the OS and converts the Path accordingly
    filedir, filename = os.path.split(filepath) # Splits the path into directory and file name

    if filedir != "": # If directory part is not empty, create the directory
        os.makedirs(filedir, exist_ok=True) 
        logger.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If file does not exist or is empty, create the file
        with open(filepath, "w") as f: # Empty file creation
            pass
        logger.info(f"Created file: {filepath}")
    else:
        logger.info(f"File already exists and is not empty: {filepath}")

