# KidneyDiseaseCNNClassifier

## Project Description

KidneyDiseaseCNNClassifier is a Python-based machine learning project for detecting kidney disease using convolutional neural networks (CNNs). The repository includes configuration management, pipeline components, utilities, and experiments for training, evaluating, and deploying a CNN model on medical data.

The project is structured to support reproducible model development with DVC, experiment tracking, and modular code under the `src/KidneyDiseaseCNNClassifier` package.

## Steps to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/antaripg/KidneyDiseaseCNNClassifier-Project.git
cd KidneyDiseaseCNNClassifier
```

### 2. Create and activate a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the environment

If your project requires any configuration values, update the files in `configs/config.yaml` or `params.yaml` before running the pipeline.

### 5. Run the project

Depending on your workflow, you can use one of the following options:

- Run the main training or experiment notebook:

```bash
jupyter notebook
```

- Run a Python script or module if available (for example, if `template.py` or other entry points exist):

```bash
python template.py
```

### 6. Use DVC for data and experiments (optional)

If the repository includes DVC pipelines and data versioning, use:

```bash
dvc pull
```

Then run the pipeline or experiment commands defined in `dvc.yaml`.

## Recommended Workflow

1. Activate the virtual environment.
2. Install dependencies.
3. Pull data and models with DVC if needed.
4. Update configuration values.
5. Run experiments via notebook or pipeline.

## Project Structure

- `src/KidneyDiseaseCNNClassifier/` - main package code
- `configs/` - configuration files
- `tests/` - unit and integration tests
- `requirements.txt` - project dependencies
- `dvc.yaml` and `params.yaml` - DVC pipeline and parameters

## Notes

- Python 3.7+ is required.
- TensorFlow 2.16 or later is used for model training.
- `dvc` and `mlflow` are included for reproducibility and tracking.


## Project Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
