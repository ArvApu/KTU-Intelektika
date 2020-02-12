# Author: Arvydas Apulskis IFF-7/13
# Module: P176B101 Intelektikos pagrindai
# Task: LAB1.

import csv
from models.dataHolder import DataHolder
from models.attribute import Attribute

# Constants
FILE_NAME = "song_data.csv"


def main():
    data_holder = DataHolder(get_header(FILE_NAME))
    read_csv(data_holder)

    attribute = Attribute()

    attribute.calc(data_holder.get_by_key('song_duration_ms'))
    attribute.print('song_duration_ms')

    attribute.calc(data_holder.get_by_key('song_popularity'))
    attribute.print('song_popularity')

    attribute.calc(data_holder.get_by_key('acousticness'))
    attribute.print('acousticness')

    attribute.calc(data_holder.get_by_key('danceability'))
    attribute.print('danceability')

    attribute.calc(data_holder.get_by_key('song_duration_ms'))
    attribute.print('energy')

    attribute.calc(data_holder.get_by_key('instrumentalness'))
    attribute.print('instrumentalness')

    attribute.calc(data_holder.get_by_key('key'))
    attribute.print('key')

    attribute.calc(data_holder.get_by_key('liveness'))
    attribute.print('liveness')

    attribute.calc(data_holder.get_by_key('loudness'))
    attribute.print('loudness')

    attribute.calc(data_holder.get_by_key('audio_mode'))
    attribute.print('audio_mode')

    attribute.calc(data_holder.get_by_key('speechiness'))
    attribute.print('speechiness')

    attribute.calc(data_holder.get_by_key('tempo'))
    attribute.print('tempo')

    attribute.calc(data_holder.get_by_key('time_signature'))
    attribute.print('time_signature')

    attribute.calc(data_holder.get_by_key('audio_valence'))
    attribute.print('audio_valence')


def get_header(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        return next(csv_reader)


def read_csv(data_holder):
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Skip header
        next(csv_reader)
        for row in csv_reader:
            data_holder.extract_row(row)


if __name__ == "__main__":
    main()
