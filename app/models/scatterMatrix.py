from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def rotate_labels(axs,n):
    for x in range(n):
        for y in range(n):
            # to get the axis of subplots
            ax = axs[x, y]
            # to make x axis name vertical
            ax.xaxis.label.set_rotation(90)
            # to make y axis name horizontal
            ax.yaxis.label.set_rotation(0)
            # to make sure y axis names are outside the plot area
            ax.yaxis.labelpad = 50


class ScatterMatrix:
    def __init__(self, data_dict):
        data_matrix = np.array([data_dict[i] for i in data_dict.keys()])
        data_matrix = np.transpose(data_matrix)

        df = pd.DataFrame(data_matrix, columns=data_dict.keys())
        axs = scatter_matrix(df, alpha=0.4, figsize=(19, 19), diagonal='hist', c='blue',
                             hist_kwds={'color': ['red']}, grid=True)

        rotate_labels(axs,len(df.columns))

        plt.subplots_adjust(top=0.99, right=0.99)
        plt.show()
