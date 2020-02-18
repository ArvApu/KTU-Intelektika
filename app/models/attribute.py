class Attribute:

    def __init__(self, name):
        self.__name = name
        self.__total_count = 0
        self.__cardinality = 0
        self.__lack_of_values_p = 0

    @staticmethod
    def __get_percentage(total, part):
        if total < 0:
            return 0

        return (100 * float(part)) / float(total)

    def get_values(self):
        return [
            self.__total_count,
            self.__lack_of_values_p,
            self.__cardinality,
        ]

    def print(self):
        print(f"{self.__name}\n")
        print(f"Total count: {self.__total_count}")
        print(f"Lack of values percentage: {self.__lack_of_values_p}%")
        print(f"Cardinality: {self.__cardinality}")

    def get_name(self):
        return self.__name

    def set_total_count(self, count):
        self.__total_count = count

    def set_cardinality(self, cardinality):
        self.__cardinality = cardinality

    def set_lack_of_values_p(self, total, part):
        self.__lack_of_values_p = self.__get_percentage(total, part)
