from models.attribute import Attribute
from collections import defaultdict


def nth_frequent(data, nth):

    appearances = defaultdict(int)

    for curr in data:
        appearances[curr] += 1

    if len(appearances) <= 0:
        return 0

    if len(appearances) < nth:
        nth = 0

    sorted_appearances = []

    for key in sorted(appearances, key=appearances.get, reverse=True):
        sorted_appearances.append([key, appearances[key]])

    return sorted_appearances[nth]


class DiscreteAttribute(Attribute):
    def __init__(self, name, data):
        super().__init__(name)
        self.__mode = 0
        self.__mode_frequency = 0
        self.__mode_percentage = 0
        self.__mode_second = 0
        self.__mode_second_frequency = 0
        self.__mode_second_percentage = 0
        self.calc(data)

    def calc(self, data):
        # Initialize variables
        unique = set()
        count = 0
        empty = 0

        # Do counting for basic calculations
        for item in data:
            if item == '' or item is None:
                empty += 1
                continue

            count += 1

            unique.add(item)

        # Set properties by founded information
        super().set_total_count(count)
        super().set_cardinality(len(unique))
        super().set_lack_of_values_p(count, empty)

        self.__mode, self.__mode_frequency = nth_frequent(data, 0)
        self.__mode_second, self.__mode_second_frequency = nth_frequent(data, 1)
        self.__mode_percentage = super().get_percentage(count, self.__mode_frequency)
        self.__mode_second_percentage = super().get_percentage(count, self.__mode_second_frequency)

    def print(self):
        super().print()
        print(f"Mode: {self.__mode}")
        print(f"Mode frequency: {self.__mode_frequency}")
        print(f"Mode percentage: {self.__mode_percentage}")
        print(f"Second mode: {self.__mode_second}")
        print(f"Second mode frequency: {self.__mode_second_frequency}")
        print(f"Second mode percentage: {self.__mode_second_percentage}")

        print("\n-------------------------------------------\n")

    def get_values(self):
        return super().get_values() + [
            self.__mode,
            self.__mode_frequency,
            self.__mode_percentage,
            self.__mode_second,
            self.__mode_second_frequency,
            self.__mode_second_percentage,
        ]

    def get_name(self):
        return super().get_name()

    def get_values_and_name(self):
        return [self.get_name()] + self.get_values()
