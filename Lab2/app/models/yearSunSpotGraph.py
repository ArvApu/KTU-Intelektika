import matplotlib.pyplot as plt


class YearSunSpotGraph:

    def __init__(self, x, y):
        plt.plot(x, y)

        plt.xlabel('Year')
        plt.ylabel('Sun activity days')

        plt.title('Days of sun activity on every year')

        plt.show()
