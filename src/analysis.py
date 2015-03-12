# Import csv file and analyze using pandas
from pylab import*

import pandas as pd

pd.set_option('display.mpl_style', 'default')
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

rcParams['figure.figsize'] = 15,5

tweets = pd.read_csv('../data/thedress.csv')


