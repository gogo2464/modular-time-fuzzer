import sqlite3
from matplotlib.figure import Figure
import pandas as pd
import numpy as np

def read_inputs(database_path, inputs):
    """
    Read TIME_TAKEN in REQUEST table where REQUEST.INPUT correspond to :inputs
    """


    conn = sqlite3.connect(database_path)
    fig = Figure(figsize=(16, 12))
    
    values_list = dict()
    for classname in inputs:
        print(classname)
        query = f"SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = ?"
        values = pd.read_sql_query(query, conn, params=classname)

        print(values["TIME_TAKEN"].tolist())
        values = values["TIME_TAKEN"].tolist()
        values = np.sort(values)
        
        # provide only enough data points to plot a smooth graph
        nbins = 16 * fig.dpi * 10
        values = values[::max(len(values) // int(nbins), 1)]
        
        values_list[classname] = values
        
    return values_list
