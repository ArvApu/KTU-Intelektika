from math import sqrt


def get_percentage(total, part):
    if total < 0:
        return 0

    return (100 * float(part)) / float(total)


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


class Attribute:

    def __init__(self):
        self.__total_count = 0
        self.__lack_of_values_p = 0
        self.__cardinality = 0
        self.__min = 0
        self.__max = 0
        self.__lower_quartile = 0
        self.__upper_quartile = 0
        self.__median = 0
        self.__average = 0
        self.__standard_deviation = 0

    def calc(self, data):

        unique = set()
        total = 0
        count = 0
        empty = 0

        minimum = data[0]
        maximum = data[0]

        for item in data:
            count += 1

            if item == '' or item is None:
                empty += 1
                continue

            unique.add(item)
            total += item

            if item > maximum:
                maximum = item
            if item < minimum:
                minimum = item

        self.__total_count = count
        self.__min = minimum
        self.__max = maximum
        self.__cardinality = len(unique)
        self.__average = round(total / count, 2)
        self.__lack_of_values_p = get_percentage(count, empty)

        data = list(filter(None, data))
        self.__standard_deviation = stddev(data)
        if count - empty > 2:
            self.__calc_quartiles(data)

    def print(self, name):
        print(f"{name}\n")

        print(f"Total count: {self.__total_count}")
        print(f"Lack of values percentage: {self.__lack_of_values_p}%")
        print(f"Cardinality: {self.__cardinality}")
        print(f"Minimal value: {self.__min}")
        print(f"Maximal value: {self.__max}")
        print(f"Lower quartile: {self.__lower_quartile}")
        print(f"Median: {self.__median}")
        print(f"Upper quartile: {self.__upper_quartile}")
        print(f"Average: {self.__average}")
        print(f"Standard deviation: {self.__standard_deviation}")
        print("\n-------------------------------------------\n")

    def __calc_quartiles(self, data):
        data = sorted(data)
        median, median_indices = find_median(data)
        q1, q1_indices = find_median(data[:median_indices[0]])
        q2, q2_indices = find_median(data[median_indices[-1] + 1:])

        self.__lower_quartile = q1
        self.__median = median
        self.__upper_quartile = q2
