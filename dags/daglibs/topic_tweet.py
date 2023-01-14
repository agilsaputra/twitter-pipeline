# import tweepy
# from tweepy.auth import OAuthHandler

consumer_key = 'SESMt1rmcaW4ULMIJ84O9Ll30'           # Add your API key here
consumer_secret = 'tyElxPKVw0sCJk7MbtfBTqh713jdabRBemeHYO7TGJsVZoLUI0'        # Add your API secret key here
access_token = '1613473924981092353-ZKvEaDoj9honytfCgaTLbjBT81uGme'           # Add your Access Token key here
access_token_secret = 'Wqc9rmVdV7yreoAIQMEEPm3Q0XUqks0FsyZ5z7htSJPXP'    # Add your Access Token secret key here

# Post a tweet
def post_tweets(tweet):
    import tweepy
    from tweepy.auth import OAuthHandler
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    return api.update_status(tweet)
