import json
import requests

def post_tweet_to_slack(current_tweet):
    """Post the tweet to the Slack channel using the webhook.
    """
    headers = {"Content-Type": "application/json"}

    #URL of the incoming webhook
    url = "<your webhook url>"

    #Extracting the text field from the tweet
    text = current_tweet['text']
    payload = {
        "text" : text
    }

    response = requests.request("POST",url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
