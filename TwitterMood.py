import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['TWITTER KEY DETAILS']['ConsumerKey']
consumer_secret = config['TWITTER KEY DETAILS']['ConsumerSecret']
access_token = config['TWITTER KEY DETAILS']['AccessToken']
access_secret = config['TWITTER KEY DETAILS']['AccessSecret']
screen_name = config['USER DETAILS']['UserNameAt']
num_users = config['USER DETAILS']['NumberOfUsers']
num_tweets = config['TWEET DETAILS']['NumTweets']

try:
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
except Exception as e:
    print(e)
    print("Check twitter key details in config and try again")


def mood(userid, count):
    tweets = []

    def get_tweets(userid):
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(count):
            cleant = clean_tweet(tweet.full_text)
            tweets.append(cleant)

    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def tweetsentiment(tweets):
        tot = 0.0
        for item in tweets:
            analysis = TextBlob(item)
            tot = tot + analysis.sentiment.polarity
        return tot

    get_tweets(userid)
    totalscore = tweetsentiment(tweets)
    return totalscore


users = []
try:
    for i in tweepy.Cursor(api.friends, screen_name=screen_name).items(50):
        while(len(users) < int(num_users)):
            if(i.protected is False):  # since private accounts throw 401 exception
                users.append(i.screen_name)
except Exception as e:
    print("Check twitter key details in config and try again")            
    exit(0)

total = 0.0
for user in users:
    total = total + mood(user, int(num_tweets))
print(total / len(users))
print(total)
