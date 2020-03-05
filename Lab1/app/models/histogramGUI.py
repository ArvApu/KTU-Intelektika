import tkinter as tk
import matplotlib.pyplot as plt


def calculate(data, name, i):

    if plt.fignum_exists(i):
        plt.clf()

    plt.figure(i)

    plt.hist(x=data, bins='auto', color='#0504aa', alpha=0.7,  rwidth=0.85)

    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {name} ')
    plt.show()


class HistogramGUI(tk.Frame):
    def __init__(self, data):
        main_window = tk.Tk()
        main_window.title('Histograms')
        main_window.geometry('400x800')

        tk.Frame.__init__(self, main_window)

        self.pack(fill="both", expand=True)

        for i, attribute in enumerate(data.get_keys()):
            # Initialize widgets
            button = tk.Button(self, text=attribute, command=lambda x=attribute, j=i: calculate(data.get_by_key(x), x, j))
            button.pack(side="top", pady=(10, 10))

    def run(self):
        self.mainloop()

