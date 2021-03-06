from math import sqrt
from models.attribute import Attribute


def find_median(sorted_list):
    indices = []

    list_size = len(sorted_list)

    if list_size % 2 == 0:
        indices.append(int(list_size / 2) - 1)  # -1 because index starts from 0
        indices.append(int(list_size / 2))

        median = (float(sorted_list[indices[0]]) + float(sorted_list[indices[1]])) / 2
        pass
    else:
        indices.append(int(list_size / 2))

        median = float(sorted_list[indices[0]])
        pass

    return median, indices
    pass


def mean(data):
    return float(sum(data) / len(data))


def variance(data):
    mu = mean(data)
    return mean([(x - mu) ** 2 for x in data])


def stddev(data):
    return round(sqrt(variance(data)), 2)


class ContinuousAttribute(Attribute):
    def __init__(self, name, data):
        super().__init__(name)
        self.__min = 0
        self.__max = 0
        self.__average = 0
        self.__standard_deviation = 0
        self.__lower_quartile = 0
        self.__median = 0
        self.__upper_quartile = 0
        self.calc(data)

    def calc(self, data):
        # Initialize variables
        unique = set()
        total = 0
        count = 0
        empty = 0
        minimum = data[0]
        maximum = data[0]

        # Do counting for basic calculations
        for item in data:
            if item == '' or item is None:
                empty += 1
                continue

            count += 1

            unique.add(item)
            total += item

            if item > maximum:
                maximum = item
            if item < minimum:
                minimum = item

        # Set properties by founded information
        super().set_total_count(count)
        super().set_cardinality(len(unique))
        super().set_lack_of_values_p(count, empty)
        self.__min = minimum
        self.__max = maximum
        self.__average = round(total / count, 2)

        # Calculate more difficult values
        data = list(filter(None, data))
        self.__standard_deviation = stddev(data)
        if count - empty > 2:
            self.__calc_quartiles(data)

    def print(self):
        super().print()
        print(f"Minimal value: {self.__min}")
        print(f"Maximal value: {self.__max}")
        print(f"Lower quartile: {self.__lower_quartile}")
        print(f"Median: {self.__median}")
        print(f"Upper quartile: {self.__upper_quartile}")
        print(f"Average: {self.__average}")
        print(f"Standard deviation: {self.__standard_deviation}")
        print("\n-------------------------------------------\n")

    def get_values(self):
        return super().get_values() + [
            self.__min,
            self.__max,
            self.__lower_quartile,
            self.__upper_quartile,
            self.__average,
            self.__median,
            self.__standard_deviation,
        ]

    def __calc_quartiles(self, data):
        data = sorted(data)
        median, median_indices = find_median(data)
        q1, q1_indices = find_median(data[:median_indices[0]])
        q2, q2_indices = find_median(data[median_indices[-1] + 1:])

        self.__lower_quartile = q1
        self.__median = median
        self.__upper_quartile = q2

    def get_name(self):
        return super().get_name()

    def get_values_and_name(self):
        return [self.get_name()] + self.get_values()
