import csv

from models.continuousAttribute import ContinuousAttribute
from models.discreteAttribute import DiscreteAttribute


class AttributeManager:

    def __init__(self):
        self.__attributes = []

    def add_attribute(self, attribute):
        self.__attributes.append(attribute)

    def print(self):
        for attribute in self.__attributes:
            attribute.print()

    def export_csv_continuous(self, filename):
        header = ['Atributo pavadinimas', 'Kiekis', 'Trūkstamos reikšmės, %', 'Kardinalumas', 'Minimali reikšmė',
                  'Maksimali reikšmė', '1-asis  kvartilis', '3-iasis  kvartilis', 'Vidurkis', 'Mediana',
                  'Standartinis nuokrypis']

        with open(filename, mode='w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(header)
            for attribute in self.__attributes:
                if isinstance(attribute, DiscreteAttribute):
                    continue
                writer.writerow(attribute.get_values_and_name())

    def export_csv_discrete(self, filename):
        header = ['Atributo pavadinimas', 'Kiekis', 'Trūkstamos reikšmės, %', 'Kardinalumas', 'Moda',
                  'Modos dažnumas', 'Moda %', '2-oji Moda', '2-osios modos dažnumas', '2-oji Moda %']

        with open(filename, mode='w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(header)
            for attribute in self.__attributes:
                if isinstance(attribute, ContinuousAttribute):
                    continue
                writer.writerow(attribute.get_values_and_name())

    def get_attribute_names(self):
        names = []
        for attribute in self.__attributes:
            names = attribute.get_name()

        return names
