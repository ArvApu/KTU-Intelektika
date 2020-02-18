from models.attribute import Attribute


class DiscreteAttribute(Attribute):
    def __init__(self, name, data):
        super().__init__(name)
        self.__mode = 0,
        self.__mode_frequency = 0,
        self.__mode_percentage = 0,
        self.__mode_second = 0,
        self.__mode_second_frequency = 0,
        self.__mode_second_percentage = 0,
        self.calc(data)

    def calc(self, data):
        a = 1

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
