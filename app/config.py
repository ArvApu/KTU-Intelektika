"""App configuration."""

import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Import file name inching path
IMPORT_FILE_NAME = os.getenv('IMPORT_FILE_NAME')

# Export file name inching path
EXPORT_FILE_NAME = os.getenv('EXPORT_FILE_NAME')

# Name of ID attribute, empty if there is no such attribute
ID_ATTRIBUTE_NAME = os.getenv('ID_ATTRIBUTE_NAME')

# Separated by comma, it is array of discrete attributes
DISCRETE_ATTRIBUTES = os.getenv('DISCRETE_ATTRIBUTES').split(',')
