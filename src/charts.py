# Open pandas dataframe and create bar chart

import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

tweets = pd.read_pickle('../data/thedress.pkl')

textList = tweets["text"].tolist()

black = [item for item in textList if "black" in item]
white = [item for item in textList if "white" in item]

white_size = len(white)
black_size = len(black)

# Create a bar chart
data = Data([
    Bar(
        x=['Black & Blue', 'White & Gold'],
        y=[black_size, white_size],
        name="The Dress",
        marker=Marker(
            color=['blue', 'gold']
        )
    )
])

plot_url = py.plot(data, filename='the-dress')











