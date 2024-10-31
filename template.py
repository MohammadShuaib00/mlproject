import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

list_of_files = [
    ".github/workflows/main.yml",
    "cloud/__init__.py",
    "cloud/s3_sync.py",
    "Data/",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_validation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/model_pusher.py",
    "src/logger/__init__.py",
    "src/logger/logging.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/constant/__init__.py",
    "src/utils/__init__.py",
    "src/utils/main_utils.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/entity/artifact_entity.py",
    "main.py",
    "templates/index.html",
    "requirements.txt",
    "setup.py",
    "DockerFile",
]

for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir}")

    # Check if file exists and if it is empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w") as f:
            pass
        logging.info(f"File created: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
