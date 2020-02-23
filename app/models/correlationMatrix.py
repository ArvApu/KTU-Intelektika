import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sn


class CorrelationMatrix:
    def __init__(self, data_dict):
        data_matrix = np.array([data_dict[i] for i in data_dict.keys()])
        data_matrix = np.transpose(data_matrix)

        fig, ax = plt.subplots(figsize=(13, 13))

        df = pd.DataFrame(data_matrix, columns=data_dict.keys())
        sn.heatmap(df.corr(), annot=True, linewidths=.5, ax=ax)

        plt.show()
