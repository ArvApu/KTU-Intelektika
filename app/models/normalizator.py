import numpy as np
import pandas as pd


def normalize(x):
    x = np.asarray(x)
    return (x - x.min()) / (np.ptp(x))


class Normalizator:
    def __init__(self, data):
        self.__data = data

    def normalize(self):
        for data in self.__data:
            self.__data[data] = normalize(self.__data[data])
        return self.__data

    def get_data(self):
        return self.__data

    def to_file(self, filename):
        df = pd.DataFrame(self.__data)
        df.to_csv(filename, encoding='utf-8', index=False, float_format='%.3f')
