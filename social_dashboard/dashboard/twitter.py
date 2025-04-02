import time
import tweepy
from tweepy.auth import OAuthHandler
from .models import Tweet

# Replace with your Bearer Token
BEARER_TOKEN = "Your_bearer_token"
def user_tweets():
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    user_id = "######"
    while True:
        try:
            response = client.get_users_tweets(id=user_id, max_results=50)
            return response.data if response.data else []
        except tweepy.TooManyRequests as e:
            reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
            wait_time = reset_time - int(time.time())
            print(f"Rate limit exceeded. Waiting {wait_time} seconds...")
            time.sleep(wait_time + 1)  # Wait until reset time
        except Exception as e:
            print(f"Error: {e}")
            break

def save_to_db():
    original_tweets = user_tweets()

    for original_tweet in original_tweets:
        # Check if tweet is NOT a retweet (API v2 structure)
        if not original_tweet.referenced_tweets or original_tweet.referenced_tweets[0].type != "retweeted":
            if not Tweet.objects.filter(tweet_id=original_tweet.id).exists():
                new_tweet = Tweet(
                    tweet_id=original_tweet.id,
                    tweet_text=original_tweet.text,
                    published_date=original_tweet.created_at,
                    is_active=True
                )