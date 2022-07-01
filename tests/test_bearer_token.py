import tweepy

BEARER_TOKEN = ''

if __name__ == '__main__':

    client = tweepy.Client(BEARER_TOKEN)

    query = '#NASDAQ'

    tweets = client.search_all_tweets(query=query, max_results=100)

    for tweet in tweets.data:
        print(tweet.text)
