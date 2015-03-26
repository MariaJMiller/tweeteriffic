# Import csv file and analyze using pandas

import pandas as pd

from pandas.tseries.offsets import DateOffset

# Import file
tweets = pd.read_csv('../data/valentine.csv')

# Change index to created_at, change time format to 12 hours.
tweets['created_at'] = pd.to_datetime(pd.Series(tweets['created_at']))
tweets.set_index('created_at', drop=False, inplace=True)
tweets.index = tweets.index.tz_localize('GMT').tz_convert('EST')
tweets.index = tweets.index - DateOffset(hours = 12)

# Save the pandas dataframe.
tweets.to_pickle('../data/valentine.pkl')







