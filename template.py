"""
Script to create the project structure for the Kidney Disease CNN Classifier project. 
It creates the necessary directories and files as specified in the list_of_files. 
If a file already exists and is not empty, it will skip creating that file and log a message 
indicating that the file already exists.
It uses the logging module to log the creation of directories and files, 
as well as to handle cases where files already exist. 
The project structure includes directories for source code, tests, 
configurations, and research notebooks, along with necessary initialization files to make them Python packages.
"""

import os
from pathlib import Path
import logging


# Logging String
# The logging configuration is set up to log messages with a specific format that includes the timestamp, 
# log level, and message content. 
# The log level is set to INFO, which means that all messages at the INFO level 
# and above (such as WARNING, ERROR, and CRITICAL) will be logged. 
# The logger is created using the __name__ variable, 
# which allows it to be used in different modules of the project while maintaining the correct context for logging messages.
logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s] %(levelname)s : %(message)s',)
logger = logging.getLogger(__name__)

# Project Name
# Project name variable to be used in the file paths for the src directory. 
# This allows for easy modification of the project name in the future by simply changing the value of this variable. 
# The project name is used to create the directory structure for the source code of the project, 
# ensuring that all source files are organized under a common directory named after the project.
projet_name = "KidneyDiseaseCNNClassifier" 

# List of  files and directories to be created
# The list_of_files variable contains the paths of all the files and directories that need to be created for the project. 
# It includes placeholder files (like .gitkeep) to ensure that certain directories are created even if they are empty. 
# The paths are constructed using the project name variable to maintain consistency and organization in the directory structure.
list_of_files = [
    ".github/workflows/.gitkeep", # This is a placeholder file to ensure that the .github/workflows directory is created in the repository. The .gitkeep file is a common convention used to keep empty directories in version control systems like Git. By including this file, we can ensure that the directory structure is maintained even if there are no actual workflow files present at the moment.
    f"src/{projet_name}/__init__.py", # init file to make the src directory a package
    f"src/{projet_name}/components/__init__.py", # init file to make the components directory a package
    f"src/{projet_name}/utils/__init__.py", # init file to make the utils directory a package
    f"src/{projet_name}/config/__init__.py", # init file to make the config directory a package
    f"src/{projet_name}/config/configuration.py", # init file to make the config directory a package
    f"src/{projet_name}/pipeline/__init__.py", # init file to make the pipeline directory a package
    f"src/{projet_name}/entity/__init__.py", # init file to make the entity directory a package
    f"src/{projet_name}/constants/__init__.py", # init file to make the constants directory a package
    "tests/__init__.py", # init file to make the tests directory a package
    "tests/unit/__init__.py", # init  # init file to make the unit tests directory a package
    "tests/integration/__init__.py", # init file to make the integration tests directory a package
    "configs/config.yaml", # Configuration file for the project
    "dvc.yaml", # DVC file for data version control
    "params.yaml", # Parameters file for the project
    "requirements.txt", # Requirements file for the project
    "setup.py", # Setup file for packaging the project
    "README.md", # README file for the project
    "research/trials.ipynb", # Jupyter notebook for research and experimentation
    "templates/index.html", # HTML template file for the project
]

# Create the files
# The code iterates through the list_of_files and creates the necessary directories and files for the project.
for filepath in list_of_files:
    filepath = Path(filepath) # Detects the OS and converts the Path accordingly
    filedir, filename = os.path.split(filepath) # Splits the path into directory and file name

    if filedir != "": # If directory part is not empty, create the directory
        os.makedirs(filedir, exist_ok=True) 
        logger.info(f"Creating directory: {filedir} for the file:: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If file does not exist or is empty, create the file
        with open(filepath, "w") as f: # Empty file creation
            pass
            logger.info(f"Creating empty file: {filepath}")
    else:
        logger.info(f"File already exists and is not empty: {filepath}")

