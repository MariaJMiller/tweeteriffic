'''
Maria Miller - mjm191@zips.uakron.edu
Idea for this project from:
http://www.danielforsyth.me/analyzing-a-nhl-playoff-game-with-twitter/
'''

import tweepy
import pymongo
import sys

from pymongo import MongoClient

# Consumer Keys and access tokens for Twitter here #

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class customStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        client = MongoClient()
        self.db = client.Single 

    def on_status(self, status):
        print status.text , "\n"

        data = {}
        data['text'] = status.text
        data['created_at'] = status.created_at
        data['geo'] = status.geo
        data['source'] = status.source

        self.db.Tweets.insert(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', 
        status_code
        return True #Don't kill the stream

    def on_timeout(self):
        print >> sys.stder, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, customStreamListener(api))
sapi.filter(track=['whyimsingle'])



