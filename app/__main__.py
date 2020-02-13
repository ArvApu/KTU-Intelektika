# Author: Arvydas Apulskis IFF-7/13
# Module: P176B101 Intelektikos pagrindai
# Task: LAB1.

import csv
from models.dataHolder import DataHolder
from models.attribute import Attribute
from models.attributeManager import AttributeManager

# Constants
IMPORT_FILE_NAME = "song_data.csv"
EXPORT_FILE_NAME = "results_export.csv"


def main():
    data_holder = DataHolder(get_header(IMPORT_FILE_NAME))
    read_csv(IMPORT_FILE_NAME, data_holder)

    attribute_manager = AttributeManager()
    attributes = data_holder.get_keys()
    for attribute in attributes:
        if attribute == 'song_name':
            continue
        attribute_manager.add_attribute(
            Attribute(attribute, data_holder.get_by_key(attribute))
        )


    attribute_manager.export_csv(EXPORT_FILE_NAME)


def get_header(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        return next(csv_reader)


def read_csv(filename, data_holder):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Skip header
        next(csv_reader)
        for row in csv_reader:
            data_holder.extract_row(row)


if __name__ == "__main__":
    main()
