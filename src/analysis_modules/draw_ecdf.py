import matplotlib as mpl
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def draw_image_ecdf(values_dict):
    """
    Generate an Empirical Cumulative Distribution Function image from a dictionary of inputs.
    
    
    """

    fig = Figure(figsize=(16, 12))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(1, 1, 1)

    for classname, val in values_dict.items():
        l = np.linspace(1. / len(val), 1, len(val))
        ax.step(val, l, where='post')
    fig.legend(values_dict.keys(), ncol=6, loc='upper center', bbox_to_anchor=(0.5, -0.15))
    
    ax.set_title("Empirical Cumulative Distribution Function")
    ax.set_xlabel("Time")
    ax.set_ylabel("Cumulative probability")
    
    formatter = mpl.ticker.EngFormatter('s')
    ax.get_xaxis().set_major_formatter(formatter)
    
    
    for classname, values in values_dict.items():
        values = np.sort(values)

        fig = Figure(figsize=(16, 12))
        nbins = 16 * fig.dpi * 10
        values = values[::max(len(values) // int(nbins), 1)]

    canvas.print_figure("ecdf_plot.png", bbox_inches="tight")
    quant = np.quantile(values, [0.01, 0.95])
    quant[0] *= 0.98
    quant[1] *= 1.02
    ax.set_xlim(quant)
    canvas.print_figure("ecdf_plot_zoom_in.png", bbox_inches="tight")
