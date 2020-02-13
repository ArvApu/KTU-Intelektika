import csv


class AttributeManager:

    def __init__(self):
        self.__attributes = []

    def add_attribute(self, attribute):
        self.__attributes.append(attribute)

    def print(self):
        for attribute in self.__attributes:
            attribute.print()

    def export_csv(self, filename):
        header = ['Atributo pavadinimas', 'Kiekis', 'Trūkstamos reikšmės, %', 'Kardinalumas', 'Minimali reikšmė',
                  'Maksimali reikšmė', '1-asis  kvartilis', '3-iasis  kvartilis', 'Vidurkis', 'Mediana',
                  'Standartinis nuokrypis']

        with open(filename, mode='w') as employee_file:
            writer = csv.writer(employee_file, delimiter=',')
            writer.writerow(header)
            for attribute in self.__attributes:
                writer.writerow(attribute.get_values_and_name())

    def get_attribute_names(self):
        names = []
        for attribute in self.__attributes:
            names = attribute.get_name()

        return names
