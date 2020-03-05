# Author: Arvydas Apulskis IFF-7/13
# Module: P176B101 Intelektikos pagrindai
# Task: LAB2.

import csv
from models.yearSunSpotGraph import YearSunSpotGraph


def main():
    year, sun_activity_days = get_data()
    YearSunSpotGraph(year, sun_activity_days)


def get_data():
    year = []
    sun_activity_days = []

    with open("./data/sunspot.txt", "r") as f:
        for line in csv.reader(f, delimiter="\t"):
            year.append(int(line[0]))
            sun_activity_days.append(int(line[1]))

    return year, sun_activity_days


if __name__ == "__main__":
    main()
