#!/usr/bin/python3
""" A function to querry Reddit API and return number of subscribers. """

import requests


def number_of_subscribers(subreddit):
    """ A function to return total number of subscribers of a subreddit. """

    # Reddit API to get subreddit information
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Setting custom user agent to avoid many request errors
    headers = {'UserAgent': 'CustomUserAgent'}

    # Api request
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return (0)
    data = response.json()
    # subscribers_count = data['data']['subscribers']
    subscribers_count = data.get('data')
    return (subscribers_count.get('subscribers'))
