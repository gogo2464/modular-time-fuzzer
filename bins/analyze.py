import numpy as np
from scipy import stats
import pandas as pd
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import os
import sys

import argparse

from src.db_crud.read import read_inputs
from src.analysis_modules.draw_ecdf import draw_image_ecdf

def main():
    parser = argparse.ArgumentParser(prog='analyze', description='Understand requests time taken by the program measure in order to detect timing attack vulnerability', epilog='Text at the bottom of help')

    parser.add_argument('-c', action='append')
    parser.add_argument('data_base')
    args = parser.parse_args()

    print("Hello World!")

    values = read_inputs(args.data_base, args.c)
    draw_image_ecdf(values)

    print("bye world")

if __name__ == "__main__":
    main()
