from plot import Plot

class HistogramPlot(Plot):
    def __init__(self, data_values, title, xlabel, ylabel, num_colors=1):
        super().__init__(data_values, title, xlabel, ylabel, num_colors)
        self.fig, self.ax = Plot.create_figure(self)
        self.bins = "sqrt"

    def set_bins(self, bins):
        self.bins = bins

    def create_plot(self):
        colors = Plot._pick_colors(self)
        self.ax.hist(self.values, bins=self.bins, color=colors, edgecolor='black')