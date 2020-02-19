# Author: Arvydas Apulskis IFF-7/13
# Module: P176B101 Intelektikos pagrindai
# Task: LAB1.

import csv
from models.dataHolder import DataHolder
from models.continuousAttribute import ContinuousAttribute
from models.discreteAttribute import DiscreteAttribute
from models.attributeManager import AttributeManager
from models.gui import GUI


# Constants
IMPORT_FILE_NAME = "song_data.csv"
EXPORT_FILE_NAME = "results_export.csv"
ID_ATTRIBUTE_NAME = 'song_name'
DISCRETE_ATTRIBUTES = ['audio_mode', 'time_signature']


def main():
    data_holder = DataHolder(get_header(IMPORT_FILE_NAME))
    read_csv(IMPORT_FILE_NAME, data_holder)
    export_data(data_holder)
    data_holder.del_by_key(ID_ATTRIBUTE_NAME)
    GUI(data_holder).run()


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


def resolve_attribute(name, data):
    if name in DISCRETE_ATTRIBUTES:
        return DiscreteAttribute(name, data)

    return ContinuousAttribute(name, data)


def export_data(data_holder):
    attribute_manager = AttributeManager()
    attributes = data_holder.get_keys()
    for attribute in attributes:
        if attribute == ID_ATTRIBUTE_NAME:
            continue

        attribute_manager.add_attribute(
            resolve_attribute(attribute, data_holder.get_by_key(attribute))
        )

    attribute_manager.export_csv(EXPORT_FILE_NAME)


if __name__ == "__main__":
    main()
