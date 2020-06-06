#!/usr/bin/env python

import logging
from config import create_api
import time
from random import choice

from tweepy import TweepError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

TWEET_PATH = '/data/bch_quotes.txt'
CHARACTER_LIMIT = 280

def submit_post(api, status):
    logger.info("Posting new tweet")
    api.update_status(status)

def retrieve_random_tweet():
    lines = open(TWEET_PATH, 'r').read().splitlines()
    tweet = choice(lines)
    if len(tweet) <= CHARACTER_LIMIT:
        return tweet
    else:
        while len(tweet) > CHARACTER_LIMIT:
            tweet = choice(lines)
        return tweet

def main():
    api = create_api()
    while True:
        tweet = retrieve_random_tweet()
        try:
            logger.info(f"publishing message: {tweet}")
            submit_post(api, tweet)
            logger.info("published message")
        except TweepError as err:
            logger.info(f"Soft fail -- TweepError: {err}")
        time.sleep(14400)

if __name__ == "__main__":
    main()