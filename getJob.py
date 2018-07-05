import json, config
from requests_oauthlib import OAuth1Session

def get_oauth():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    oauth = OAuth1Session(CK, CS, AT, ATS) #認証処理
    return oauth

def tweet_search(search_word, oauth):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": "100"
        }
    responce = oauth.get(url, params = params)
    if responce.status_code != 200:
        print("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

def write_text(text):
    f = open('job.txt', 'a')
    f.write(text)
    f.close

oauth = get_oauth()
search_word = "#就活 #大学生"
tweets = tweet_search(search_word, oauth)

pluch_texts = {}
for tweet in tweets['statuses']:
    pluch_texts[tweet['id']] = tweet['text']
    write_text(tweet['text'])


