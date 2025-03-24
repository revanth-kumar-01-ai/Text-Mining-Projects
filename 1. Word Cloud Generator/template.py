import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Project name
project_name = "word_cloud_project"

# List of required files and directories
list_of_files = [
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/main.py",
    f"{project_name}/src/preprocessing.py",
    f"{project_name}/src/wordcloud_generator.py",
    f"{project_name}/artifacts/__init__.py",
    f"{project_name}/output/__init__.py",
    f"{project_name}/research/trials.ipynb",
    f"{project_name}/StreamLit/app.py",
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md"
]

# Create files and directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

print("✅ Project structure created successfully! 🚀")
