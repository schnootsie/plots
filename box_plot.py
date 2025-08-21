from plot import Plot

class BoxPlot(Plot):
    def __init__(self, data_values, categories, title, xlabel, ylabel, num_colors=1):
        super().__init__(data_values, title, xlabel, ylabel, num_colors)
        self.fig, self.ax = Plot.create_figure(self)
        self.categories = categories
        self.outliers = 1.5

    def create_plot(self):
        colors = Plot._pick_colors(self)
        medianprops = dict(linestyle='-', linewidth=3, color='black')
        bplot = self.ax.boxplot(self.values, labels=self.categories, widths=0.5, medianprops=medianprops,patch_artist=True, whis=self.outliers)
        for patch in bplot['boxes']:
            patch.set_facecolor(colors[0])
