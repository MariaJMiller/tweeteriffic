# View words frequently associated with topic in Tweets

import pandas as pd
import nltk
from nltk.corpus import stopwords
import pickle

tweets = pd.read_pickle('../data/valentine.pkl')

textList = tweets["text"]

stop = set(stopwords.words('english'))

tokens = []

for txt in textList:
    tokens.extend([t.lower().strip(";,.") for t in txt.split()])

filtered_tokens = [w for w in tokens if not w in stop]

freq_dist = nltk.FreqDist(filtered_tokens)



