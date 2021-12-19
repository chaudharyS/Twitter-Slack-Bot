import json
import requests

#The TwitterHashtagSearch class takes the query to search through tweets
class TwitterHashtagSearch:

    # The constructor for the class. It takes the query as the a
    # parameter and then sets it as an instance variable
    def __init__(self, query):
        self.query = query

    #Get the bearer token from the config.json file
    def get_bearer_token(self):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
            bearer_token = config["BEARER_TOKEN"]
            return bearer_token
        except:
            print("Problem loading config.json")
            return None

    #Search Twitter to find the query to get the latest 20 tweets matching the query
    def search_twitter(self):
        bearer_token = self.get_bearer_token()
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        tweet_fields = "tweet.fields=text,author_id,created_at"

        #The max_results parameter can take any value between 10 and 100
        url = "https://api.twitter.com/2/tweets/search/recent?max_results=20&query={}&{}".format(
            self.query, tweet_fields
        )
        response = requests.request("GET", url, headers=headers)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return response.json()
