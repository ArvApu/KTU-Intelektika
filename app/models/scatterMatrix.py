from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class ScatterMatrix:
    def __init__(self, data_dict):
        data_matrix = np.array([data_dict[i] for i in data_dict.keys()])
        data_matrix = np.transpose(data_matrix)

        df = pd.DataFrame(data_matrix, columns=data_dict.keys())
        scatter_matrix(df, alpha=0.4, figsize=(19, 19), diagonal='hist', c='blue', hist_kwds={'color': ['red']}, grid=True)
        plt.show()
