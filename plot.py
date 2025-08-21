# general plot class
#     - has general things that all plots have
# create other classes like boxplot that inherits the general plot class
#     - this has things that are specific to plots

# initialize figure
# pick colors
# set font
# set font size

# from matplotlib.font_manager import FontProperties
# font = FontProperties(family='Times New Roman', style='italic')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class Plot():
    def __init__(self, data_values, title, xlabel, ylabel, num_colors):
        self.values = data_values
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xfigsize = 12
        self.yfigsize = 8
        self.titlesize = 30
        self.labelsize = 28
        self.textsize = 20
        self.font = "Computer Modern Roman"
        self.num_colors = num_colors
        self.color_scale = "divergent"

    def _pick_colors(self):
        if self.num_colors == 1:
            return ['#4DA1A9']
        elif self.num_colors == 2:
            return ['#4DA1A9', '#611C35']
        elif self.num_colors == 3:
            return ['#4DA1A9', '#FFB757', '#611C35']
        elif self.num_colors == 4:
            return ['#335A85', '#4DA1A9', '#F7713B', '#611C35']
        elif self.num_colors == 5:
            return ['#335A85', '#4DA1A9', '#D7E8BA', '#F7713B', '#611C35']
        elif self.num_colors == 6:
            return ['#335A85', '#4DA1A9', '#D7E8BA', '#FFB757', '#F7713B', '#611C35']
        elif self.num_colors > 6 or self.color_scale=="sequential":
            # cmap = mpl.colormaps.get_cmap('Blues')
            colors = ['#335A85', '#4DA1A9', '#D7E8BA']
            cmap = LinearSegmentedColormap.from_list("mycmap", colors)
            return [cmap(i/(self.num_colors-1)) for i in list(range(0,self.num_colors))]

    # CHECK: https://realpython.com/python-getter-setter/
    def set_xfigsize(self, size):
        self.xfigsize = size

    def set_yfigsize(self, size):
        self.yfigsize = size

    def set_titlesize(self, size):
        self.titlesize = size

    def set_labelsize(self, size):
        self.labelsize = size

    def set_textsize(self, size):
        self.textsize = size

    # TODO: how to set colors?
    # def set_colors(self, colors):

    def create_figure(self):
        # TODO: Handling LaTeX
        # try:
        #     plt.rc('font',**{'family':'serif','serif':[self.font],'size': self.textsize})
        #     plt.rc('text', usetex=True)
        # except ModuleNotFoundError:
        plt.rc('font',**{'family':'serif','size': self.textsize})
        #     plt.rc('text', usetex=False)
        #     print("LaTeX not found. Proceeding without it.")
        fig, ax = plt.subplots(figsize=(self.xfigsize, self.yfigsize))
        ax.set_title(self.title, fontsize=self.titlesize, pad=20)
        ax.set_xlabel(self.xlabel, fontsize=self.labelsize, labelpad=10)
        ax.set_ylabel(self.ylabel, fontsize=self.labelsize, labelpad=10)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        return (fig, ax)

    def save_fig(self, path):
        # TODO: create path if not there
        plt.savefig(path,
                    transparent=False,
                    bbox_inches='tight',
                    pad_inches=0.25)