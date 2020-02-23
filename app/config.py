"""App configuration."""

import os
import argparse
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


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-hg', '--histograms', dest='histograms_enabled', action='store_true',
                        help='Toggle usage of histograms')
    parser.add_argument('-sm', '--scatter', dest='scatter_matrix_enabled', action='store_true',
                        help='Toggle usage of scatter matrix')
    parser.add_argument('-cm', '--correlation', dest='correlation_matrix_enabled', action='store_true',
                        help='Toggle usage of correlation matrix')

    return parser.parse_args()
