import time
import jsonpickle as jsonpickle
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import twitter_credentials


def limit_handled(cursor):
    while True:
        try:
            print("Trying...")
            yield cursor.next()
        except tweepy.TweepError:
            print("Rate Limit Error")
            time.sleep(15 * 60)


if __name__ == '__main__':
    # This handles Twitter authentication and the connection to Twitter Streaming API
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    if not api:
        print("Problem connecting to API")
        exit(0)

    tweetCount = 0
    searchQuery = '#kashmir OR #illegalindianoccupation ' \
                  'OR #savekashmir OR #freedomforkashmir ' \
                  'OR #KashmirIsBleeding OR #kashmirisbleeding OR #jihad OR #lashkar-e-taiba OR #ISIS ' \
                  'OR #isis OR #taliban OR #islamists OR #Al Qaeda ' \
                  'OR #Al-Shabaab OR #jaesh OR #islamicState OR #kashmir OR #FreedomForKashmir OR #KashmirCrisis ' \
                  'OR #wahhabism OR #goharshahi OR #wahhabi '

    # Open a text file to save the tweets to
    with open('TerrorismData31032019', 'w') as f:

        # Tell the Cursor method that we want to use the Search API (api.search)
        # Also tell Cursor our query, and the maximum number of tweets to return
        # for tweet in tweepy.Cursor(api.search, q=searchQuery).items(50000):
        #     f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
        #     tweetCount += 1

        for tweet in limit_handled(tweepy.Cursor(api.search, q=searchQuery).items(50000)):
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        # Display how many tweets we have collected
        print("Downloaded {0} tweets".format(tweetCount))

