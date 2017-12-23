import tweepy, random, sys, re
from datetime import datetime
from threading import Timer
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
def connect():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def generate_markov(text):
    chain = {}
    
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    return chain

def generate_message(chain):
    count = 20

    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    
    return message

def tweet_message():
    twitter = connect()
    
    with open('online__davids_tweets.txt', 'r') as myfile:
        data=myfile.read()
    
    while(True):
        try:
            markov = generate_markov(data)
            msg = generate_message(markov)
            while "@" in msg:
                msg = generate_message(markov)
            print(msg)
            twitter.update_status(status=msg)
            break
        except tweepy.error.TweepError as e:
            print(e)
            continue

if __name__ == '__main__':
    
    tweet_message()
