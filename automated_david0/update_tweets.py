import tweepy
# Import our Twitter credentials from credentials.py
from credentials import *

def update_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    tweetidset = set()
    
    with open('online__david_tweetids.txt', 'r') as f:
        for line in f:
            tweetidset.add(line.strip('\n'))

    #initialize a list to hold all the tweepy Tweets
    alltweets = []	

    #make initial request for most recent tweets
    new_tweets = api.user_timeline(screen_name = screen_name,count=50)

    #save most recent tweets
    alltweets.extend(new_tweets)
    
    outtweets = ""
    tweetids = ""

    for tweet in alltweets:
        if str(tweet.id) not in tweetidset and "@automated__david:" not in str(tweet.text):
            outtweets = outtweets + " " + str(tweet.text)
            tweetids = tweetids + "\n" + str(tweet.id)
    
    print(outtweets)
    print('=====')
    print(tweetids)
    
    with open(screen_name+'s_tweets.txt', 'a') as f:
        f.write(outtweets)
        
    with open(screen_name+'_tweetids.txt', 'a') as f:
        f.write(tweetids)
        
    pass


if __name__ == '__main__':
    #get all tweets by @name
    update_tweets("online__david")