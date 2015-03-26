# View words frequently associated with topic in Tweets

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist

tweets = pd.read_pickle('../data/valentine.pkl')

textList = tweets["text"]

tokens = []

for txt in textList:
    tokens.extend([t.lower().strip(";,.") for t in txt.split()])

#filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]

