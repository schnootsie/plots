import matplotlib.ticker as ticker
from plot import Plot

class BarPlot(Plot):
    def __init__(self, data_values, categories, title, xlabel, ylabel, num_colors=1):
        super().__init__(data_values, title, xlabel, ylabel, num_colors)
        self.fig, self.ax = Plot.create_figure(self)
        self.categories = categories

    def create_plot(self):
        colors = Plot._pick_colors(self)
        self.ax.bar(self.categories, self.values, edgecolor="black",color=colors)
        self.ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    
    def add_labels(self):
        for i in range(len(self.categories)):
            self.ax.text(i, self.values[i], self.values[i], ha='center', va='bottom')

    def add_errorbars(self, error_values):
        self.ax.errorbar(self.categories, self.values, yerr=error_values, capsize=7, fmt='none', color="black")

    # Can I add a horizontal option