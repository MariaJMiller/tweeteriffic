# View words frequently associated with topic in Tweets

import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

db = pd.read_pickle('../data/thedress.pkl')

textList = db["text"].toList()

