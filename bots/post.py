#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

import tweepy
import logging
from config import create_api
import time
import collections
from random import shuffle
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

TWEET_PATH = '../data/bch_quotes.txt'
CHARACTER_LIMIT = 280

def filter_curated_tweets(tweet):
    clean_tweet = re.sub('\n', '', tweet)
    return clean_tweet

def load_message_deque():
    with open(TWEET_PATH, 'r') as f:
        raw_tweets = [
            filter_curated_tweets(line) for line in f
        ]
    shuffle(raw_tweets)
    return collections.deque((
        item for item in raw_tweets
        if len(item) <= CHARACTER_LIMIT
    ))

def submit_post(api, status):
    logger.info("Posting new tweet")
    api.update_status(status)

def main():
    api = create_api()
    message_deque = load_message_deque()
    while True:
        tweet = message_deque[0]
        logger.info(f"publishing message: {tweet}")
        submit_post(api, tweet)
        logger.info("rotating tweet deque")
        message_deque.rotate()
        time.sleep(60)

if __name__ == "__main__":
    main()