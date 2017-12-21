import tweepy
# Import our Twitter credentials from credentials.py
from credentials import *

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []	

    #make initial request for most recent tweets (200 is the maximum allowed by the API)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    #keep getting tweets until there are no tweets left
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    #transform the tweets and ids into strings
    outtweets = ""

    first = True
    for tweet in alltweets:
        if first:
            tweetids = str(tweet.id)
            first = False
        else:
            tweetids = tweetids + "\n" + str(tweet.id)

        outtweets = outtweets + " " + str(tweet.text)

    #write the file
    with open(screen_name+'s_tweets.txt', 'w') as f:
        f.write(outtweets)
        
    with open(screen_name+'_tweetids.txt', 'w') as f:
        f.write(tweetids)
    
    pass


if __name__ == '__main__':
    #get all tweets by @name
    get_all_tweets("online__david")