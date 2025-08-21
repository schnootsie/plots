import csv
from bar_plot import BarPlot
from hist_plot import HistogramPlot
from box_plot import BoxPlot

# BAR PLOT
with open("./sample_data/cat_count.csv", "r") as f:
    file = csv.reader(f, delimiter=",")
    categories = []
    values = []
    for line in file:
        categories.append(str(line[0]))
        values.append(int(line[1]))
    
my_bar = BarPlot(values, categories, "Favorite Fruits", "Fruit", "Counts")
my_bar.create_plot()
my_bar.save_fig("./sample_plots/bar.png")

my_bar.create_plot()
my_bar.add_labels()
my_bar.save_fig("./sample_plots/bar_labeled.png")

my_bar.create_plot()
my_bar.add_errorbars([3,5,2,4])
my_bar.save_fig("./sample_plots/bar_error.png")

# HISTOGRAM
with open("./sample_data/quant.csv", "r") as f:
    file = csv.reader(f, delimiter=",")
    values = []
    for line in file:
        values.append(float(line[0]))
    
my_hist = HistogramPlot(values, "Strawberry Weights", "Weight (g)", "Number of Strawberries")
my_hist.create_plot()
my_hist.save_fig("./sample_plots/histogram.png")

# BOX PLOT
with open("./sample_data/multi_quant.csv", "r") as f:
    file = csv.reader(f, delimiter=",")
    values1 = []
    values2 = []
    values3 = []
    for line in file:
        values1.append(float(line[0])*10)
        values2.append(float(line[1])*10)
        values3.append(float(line[2])*10)
values = [values1, values2, values3]
    
my_box = BoxPlot(values, ["Granny Smith", "Pink Lady", "Golden Delicious"], "Apples Weights", "Apples", "Weight (g)")
my_box.create_plot()
my_box.save_fig("./sample_plots/box.png")