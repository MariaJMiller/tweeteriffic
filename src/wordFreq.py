# View words frequently associated with topic in Tweets

import pandas as pd
import nltk
from nltk.corpus import stopwords

# Get tweets previously saved.
tweets = pd.read_pickle('../data/valentine.pkl')

textList = tweets["text"]

stop = set(stopwords.words('english'))

# Add stopwords not included in nltk corpus.
stop.add('&amp')
stop.add('rt')
stop.add("it's")

tokens = []

# Remove some punctuation.
for txt in textList:
    tokens.extend([t.lower().strip(";,.") for t in txt.split()])

# Remove stop words.
filtered_tokens = [w for w in tokens if not w in stop]

# Create a frequency distribution of words.
freq_dist = nltk.FreqDist(filtered_tokens)

# Get the top 50 most frequently tweeted words.
top_words = freq_dist.most_common(50)



