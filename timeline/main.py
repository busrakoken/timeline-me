import twitter
import os

consumer_key=os.environ['API_KEY']
consumer_secret=os.environ['API_SECRET_KEY']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

api = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token,
                    access_token_secret=access_token_secret)

result = api.GetSearch(
    raw_query="q=mentoring%20&result_type=recent&since=2019-02-23&count=10")

for i in result:
    print(i.text)