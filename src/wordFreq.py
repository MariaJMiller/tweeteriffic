#Create a frequency distribution for tweets.
import pandas as pd
import nltk
from nltk.corpus import stopwords

tweets = pd.read_pickle('../data/single.pkl')

textList = tweets['text']

stop = set(stopwords.words('english'))

stop.add('&amp')
stop.add('amp')
stop.add('rt')
stop.add("it's")
stop.add('-')

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

print top_words