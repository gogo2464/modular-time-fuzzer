import numpy as np
from scipy import stats
import pandas as pd
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import argparse
import sqlite3

parser = argparse.ArgumentParser(prog='analyze', description='Understand requests time taken by the program measure in order to detect timing attack vulnerability', epilog='Text at the bottom of help')

parser.add_argument('-c', action='append')
parser.add_argument('data_base')
args = parser.parse_args()

def generate_ecdf_plot():
    """
    Generate ECDF plot comparing distributions of the test classes.
    
    Read the database filled as argument to the command line. Read the database and generate an ecdf plot graph to visualize any detectable time based side channel vulnerability.
    """

    fig = Figure(figsize=(16, 12))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(1, 1, 1)

    columns = args.c

    conn = sqlite3.connect(args.data_base)
    
    fig = Figure(figsize=(16, 12))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(1, 1, 1)
    for classname in args.c:    
        print(classname)
        query = f"SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = ?"
        values = pd.read_sql_query(query, conn, params=classname)
        
        print(values["TIME_TAKEN"].tolist())
        values = values["TIME_TAKEN"].tolist()
        values = np.sort(values)
        
        # provide only enough data points to plot a smooth graph
        nbins = 16 * fig.dpi * 10
        values = values[::max(len(values) // int(nbins), 1)]
        levels = np.linspace(1. / len(values), 1, len(values))
        ax.step(values, levels, where='post')
    
    fig.legend(args.c, ncol=6, loc='upper center', bbox_to_anchor=(0.5, -0.15))
    
    ax.set_title("Empirical Cumulative Distribution Function")
    ax.set_xlabel("Time")
    ax.set_ylabel("Cumulative probability")

    formatter = mpl.ticker.EngFormatter('s')
    ax.get_xaxis().set_major_formatter(formatter)

    canvas.print_figure("ecdf_plot.png", bbox_inches="tight")
    quant = np.quantile(values, [0.01, 0.95])
    quant[0] *= 0.98
    quant[1] *= 1.02
    ax.set_xlim(quant)
    canvas.print_figure("ecdf_plot_zoom_in.png", bbox_inches="tight")


def main():
    generate_ecdf_plot()
    print("Hello World!")

if __name__ == "__main__":
    main()
