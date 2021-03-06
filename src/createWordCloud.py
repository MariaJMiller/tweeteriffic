# View words frequently associated with topic in Tweets
# Create word cloud using module wordCloud

import pandas as pd
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread

# Get tweets previously saved.
tweets = pd.read_pickle('../data/valentine.pkl')

# Create single string from tweets.
words = ' '.join(tweets['text'])

# remove URLs, RTs, and twitter handles
no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

stop = set(stopwords.words('english'))

# Import image for mask
# http://www.stencilry.org/stencils/symbols/hearts/heart+1.jpg
heart_mask = imread('../images/heart.png', flatten=True)

# Add stopwords not included in nltk corpus.
stop.add('&amp')
stop.add('amp')
stop.add('rt')
stop.add("it's")
# stop.add('-')
# stop.add('WhyImSingle')
stop.add("valentine's")
stop.add('day')
stop.add('valentine')

# Create word cloud.
word_cloud = WordCloud(
  font_path='/Users/MariaJ/Library/Fonts/BD_Cartoon_Shout.ttf',
  stopwords=stop,
  width=1800,
  height=1600
  ).generate(no_urls_no_tags)
plt.imshow(word_cloud)
plt.axis('off')
plt.savefig('../images/val.png', dpi=300)
plt.show()



