#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
from time import sleep
import pandas as pd
import re
import sys

def get_oauth():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    oauth = OAuth1Session(CK, CS, AT, ATS)
    return oauth

def tweet_search(search_word, oauth, max_id):
    print('max_id:', max_id)
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": "100",
        'max_id': max_id,
        }
    responce = oauth.get(url, params = params)
    if responce.status_code != 200:
        return None
    tweets = json.loads(responce.text)
    return tweets

def prepare_tweet_list(tweet):
    text = tweet['text']
    return text


def create_dataframe(data_list):
    df = pd.DataFrame([data_list])
    return df

def is_same_max_id(max_id, current_max_id):
    return max_id == current_max_id

def is_end_loop(count):
    return count >= 60

def is_id_error(max_id, current_max_id):
    try:
        return is_same_max_id(max_id, current_max_id)
    except IndexError:
        return True


df = pd.DataFrame()
search_word_list = config.SEARCH_WORD_LIST
for index, search_word in enumerate(search_word_list):
    max_id = -1
    count = 0
    while True:
        oauth = get_oauth()
        tweets = tweet_search(search_word, oauth, max_id)

        for tweet in tweets['statuses']:
            if re.match('RT', tweet['text']):
                continue
            append_list = prepare_tweet_list(tweet)
            df_current = create_dataframe(append_list)
            df = df.append(df_current)

        try:
            current_max_id = tweets['statuses'][-1]['id']
        except :
            break
        if is_id_error(max_id, current_max_id): break
        max_id = tweets['statuses'][-1]['id']
        count += 1
        df.to_csv(sys.argv[1], mode='a', index=None, header=None)
        print(search_word, 'の探索回数は', count, '回目です')
        if is_end_loop(count): break
        sleep(10)


