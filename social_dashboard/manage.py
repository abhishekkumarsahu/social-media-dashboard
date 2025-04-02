#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import tweepy


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_dashboard.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Replace these with your own credentials
consumer_key = 'cPvZ7cMkuSBKITi4z8m7Gt8Xc'
consumer_secret = 'U09Xc41yfqkZfGya1oc46xtsjeBHzq0jU7OhqTlPPbFzE1iIEI'
access_token = '1905320725264924672-SZHa0qqcZ64SAl5qfLX1WdP3iugOP7'
access_token_secret = 'isegGXLSwxFvv0glQbIi5TAEMqz29oHFiwRdhemIIACRq'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API Initialization
api = tweepy.API(auth, wait_on_rate_limit=True)