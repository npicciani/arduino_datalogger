import plotly as py
import pandas as pd
import numpy as np

import plotly.plotly as py
import plotly.tools as plotly_tools
import plotly.graph_objs as go

import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
import matplotlib.pyplot as plt

from IPython.display import HTML


# Calculate moving average
def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')


# Plot temperature scatter data and moving average
xy_data = go.Scatter( x=x, y=y, mode='markers', marker=dict(size=4), name='AAPL' )
# vvv clip first and last points of convolution
mov_avg = go.Scatter( x=x[5:-4], y=ma[5:-4], \
                  line=dict(width=2,color='red',opacity=0.5), name='Moving average' )
data = [xy_data, mov_avg]

py.iplot(data, filename='apple stock moving average')