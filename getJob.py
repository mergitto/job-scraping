#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
from time import sleep
import pandas as pd
from pprint import pprint
import re

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
        print("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

def prepare_tweet_list(tweet):
    tweet_id = tweet['id']
    text = tweet['text']
    created_at = tweet['created_at']
    append_list = [tweet_id, text, created_at]
    return append_list


def create_dataframe(data_list, columns):
    df = pd.DataFrame(
        [data_list],
        columns=columns
    )
    return df

columns = ['id', 'tweet', 'created_at']
df = pd.DataFrame(columns=columns)
search_word_list = ["就活 内定", "就活 大学生", "内定 資格", "新卒 内定"]
for search_word in search_word_list:
    max_id = -1
    count = 0
    while True:
        oauth = get_oauth()
        tweets = tweet_search(search_word, oauth, max_id)

        for tweet in tweets['statuses']:
            if re.match('RT', tweet['text']):
                continue
            append_list = prepare_tweet_list(tweet)
            df_current = create_dataframe(append_list, columns)
            df = df.append(df_current)

        if max_id == tweets['statuses'][-1]['id']:
            break
        max_id = tweets['statuses'][-1]['id']
        count += 1
        df.to_csv('./job.csv', mode='a')
        print(search_word, 'の探索回数は', count, '回目です')
        if count >= 60:
            break
        sleep(60)


