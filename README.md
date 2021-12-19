# Twitter-Slack-Bot
Welcome to the Twitter Slack Bot repository.

This is a simple application made using the APIs from Twitter and Slack.

## What is Twitter-Hashtag-Search?
Twitter Slack Bot is designed to search all the tweets with the a particular hashtag and automatically send them to a Slack channel.

It uses a combination of the Twitter API, and Slack Incoming Webhooks to achieve that. Below is a result of the final integration in action.
![image](https://user-images.githubusercontent.com/26349309/146691362-cc842b9d-9727-4a6f-919e-3d10a553950a.png)

## What you'll need before getting started?
1. Twitter Developer Account
2. A Slack Workspace that you have the ability to install applications into.
3. A SlackBot
4. Python 3.6+. You can check your Python version by running the following command in your terminal:
```
python3 --version
```
5. Flask

## What are the files in the repository?
1. config.json - Stores the bearer token. It is good practice to have a config file to store access keys, secret tokens, etc. It's bad practice to place your bearer token directly into the script.
2. twitterhashtagsearch.py - Defines a class that takes the query to search through tweets.
3. slackmessenger.py - Defibes the function to post a tweet to the Slack channel using the webhook.
4. requirements.txt - Installation requirements for this app.

## References
- How To Build a Slackbot in Python on Ubuntu 20.04. by Mason Egger
- How to Use the Twitter API to Create a Hashtag Search Bot by Sean Keegan
- Twitter API Documentation
