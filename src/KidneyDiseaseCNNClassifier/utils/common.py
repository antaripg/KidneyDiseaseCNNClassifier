import os
from box.exceptions import BoxValueError
import yaml
from src.KidneyDiseaseCNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty or cannot be read.
    
    Returns:
        ConfigBox: A ConfigBox object containing the contents of the yaml file.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"The yaml file at {path_to_yaml} is empty.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error reading the yaml file at {path_to_yaml}: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the yaml file at {path_to_yaml}: {e}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Dictionary to save as JSON.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.
    Returns:
        ConfigBox: Contents of the JSON file as a ConfigBox object.
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
        logger.info(f"JSON file loaded from: {path}")
        if content is None:
            raise ValueError(f"The JSON file at {path} is empty.")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to save the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:  
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path, unit: str = "kb") -> float:
    """
    Returns the size of a file in the specified unit.

    Args:
        path (Path): Path to the file.
        unit (str): Unit for size ('kb', 'mb', 'gb'). Default is 'kb'.

    Returns:
        float: Size of the file in the specified unit.
    """
    size_in_bytes = os.path.getsize(path)
    if unit == "kb":
        return size_in_bytes / 1024
    elif unit == "mb":
        return size_in_bytes / (1024 ** 2)
    elif unit == "gb":
        return size_in_bytes / (1024 ** 3)
    else:
        raise ValueError(f"Unsupported unit '{unit}'. Use 'kb', 'mb', or 'gb'.")

@ensure_annotations
def encode_image_to_base64(image_path: Path) -> str:
    """
    Encodes an image file to a base64 string.

    Args:
        image_path (Path): Path to the image file.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        try:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            logger.info(f"Image at {image_path} encoded to base64.")
            return encoded_string
        except Exception as e:
            logger.error(f"Failed to encode image at {image_path} to base64: {e}")
            raise

@ensure_annotations
def decode_base64_to_image(encoded_string: str, output_path: Path):
    """
    Decodes a base64 string back to an image file.

    Args:
        encoded_string (str): Base64 encoded string of the image.
        output_path (Path): Path to save the decoded image file.
    """
    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory for output image at: {output_path.parent}")
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(encoded_string))
        logger.info(f"Base64 string decoded and saved to {output_path}.")
            
