import os
import logging
import json
from flask import Flask
from twitterhashtagsearch import TwitterHashtagSearch
from slackmessenger import post_tweet_to_slack

app = Flask(__name__)

if __name__ == "__main__":
	# Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    #Define the query you want to search twitter for. This can be a hashtag, terms, etc.
    query = "%23spidermannowayhome"

    #The twitter_bot object creates an instance of TwitterHashtagSearch 
    twitter_bot = TwitterHashtagSearch(query)

    json_response = twitter_bot.search_twitter()

    #pretty printing
    #Feel free to delete this line if you like 
    print(json.dumps(json_response, indent=4, sort_keys=True))

    tweets = json_response['data']

    #Slack has a character limit on the body of a request. So we can't dump the content of 20
    #tweets at once. Hence, we end up looping through the array of 20 tweets and calling 
    #this request 20 times. 
    for tweet in tweets:
    	post_tweet_to_slack(tweet)

    app.run(host='0.0.0.0', port=3000)