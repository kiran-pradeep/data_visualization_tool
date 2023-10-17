import matplotlib.pyplot as plt

def set_basic(ymax, title_x, title_y, grid='on'):
    plt.axis(ymax=ymax)
    plt.xlabel(title_x)
    plt.ylabel(title_y)
    plt.grid(b=grid)
    plt.legend(loc=0)
    

def line_plot(x, y, label, ls, color, marker, markersize, mew, linewidth):
    plt.plot(x, y, label=label, ls=ls, color=color, marker=marker, markersize=markersize, mew=mew, linewidth=linewidth)


def save_graph(out_path):
    plt.savefig(out_path, bbox_inches='tight')