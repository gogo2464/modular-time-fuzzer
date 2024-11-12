import matplotlib as mpl
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import matplotlib.pyplot as plt

def draw_image_means(values_dict):
    """
    Generate a mean image.
    """
    input_len = len(values_dict.items())
    
    fig, ax = plt.subplots()
    canvas = FigureCanvas(fig)
    
    means = dict()
    for classname, vals in values_dict.items():
        means[classname] = sum(vals) / len(vals)
    
    ax.bar(list(means.keys()), list(means.values()), label=classname) #ax.step(list(means.keys()), list(means.values()), where='post', label=classname)
    #ax.legend(values_dict.keys(), ncol=6, loc='upper center', bbox_to_anchor=(0.5, -0.15))
    
    ax.set_xlabel("X - Inputs")
    ax.set_ylabel("Y - Time")
    ax.set_title("Average time taken for each inputs for {0} requests".format(len(list(values_dict[list(values_dict.keys())[0]]))))
    ax.grid(False)
    
    fig.savefig("horizontal_sticks.png")
