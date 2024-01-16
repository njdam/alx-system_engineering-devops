#!/usr/bin/python3
""" A function to querry Reddit API and return number of subscribers. """

import requests


URL = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    """ A function to return total number of subscribers of a subreddit."""
    api_headers = {
            'Accept': 'application/json',
            'User-Agent': ' '.join([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'AppleWebKit/537.36 (KHTML, like Gecko)',
                'Chrome/120.0.0.0',
                'Safari/537.36',
                'Gecko/geckotrail',
                'Firefox/firefoxversion'
                ])
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
