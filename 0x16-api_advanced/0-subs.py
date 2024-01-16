#!/usr/bin/python3
""" A function to querry Reddit API and return number of subscribers. """

import requests


def number_of_subscribers(subreddit):
    """ A function to return total number of subscribers of a subreddit."""
    URL = 'https://www.reddit.com'

    api_headers = {
            'Accept': 'application/json',
            'User-Agent': 'CustomUserAgent'
            }
    response = requests.get(
            '{}/r/{}/about/.json'.format(URL, subreddit),
            headers=api_headers,
            allow_redirects=False
            )
    results = response.json()

    if response.status_code == 200:
        return (results['data']['subscribers'])
    return (0)
