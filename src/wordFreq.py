#!/usr/bin/env python2

# View words frequently associated with topic in Tweets

import pandas as pd
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Get tweets previously saved.
tweets = pd.read_pickle('../data/valentine.pkl')

words = ' '.join(tweets['text'])

# remove URLs, RTs, and twitter handles
no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

stop = set(stopwords.words('english'))

# Add stopwords not included in nltk corpus.
stop.add('&amp')
stop.add('rt')
stop.add("it's")

# Create word cloud.
word_cloud = WordCloud(
  font_path='/Users/MariaJ/Library/Fonts/NASHVILL.TTF'
  ).generate(no_urls_no_tags)
plt.imshow(word_cloud)
plt.axis('off')
plt.savefig('./word_cloud_first', dpi=300)
plt.show()


# Create a frequency distribution for tweets.
# tokens = []
#
# # Remove some punctuation.
# for txt in textList:
#     tokens.extend([t.lower().strip(";,.") for t in txt.split()])
#
# # Remove stop words.
# filtered_tokens = [w for w in tokens if not w in stop]
#
# # Create a frequency distribution of words.
# freq_dist = nltk.FreqDist(filtered_tokens)
#
# # Get the top 50 most frequently tweeted words.
# top_words = freq_dist.most_common(50)


