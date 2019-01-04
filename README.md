# Twitter Mood Analysis

A python script that analyses the tweets of the people that you are following and gives your timeline a score based on the sentiments of their tweets.

Requires Python 3.x

### Instructions:
* Install requirements (`pip install -r requirements.txt`)
* Get your twitter keys and add details to the config.ini file
* Add the @ of the user to be analysed in `UserNameAt` in config.ini
* `NumTweets` is the number of tweets from each account to be analysed (15 is a good option)
* `NumberOfUsers` is the number of people you are following to be analysed (30 is good)
* Run `python TwitterMood.py` and wait for results (may take some time)

Please allow the program to run for a while as it implements cleaning and sentiment analysis on hundreds of tweets.
