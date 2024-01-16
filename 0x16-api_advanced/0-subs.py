#!/usr/bin/python3
'''A function to querry Reddit API and return number of subscribers.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''A reddit's base API URL.
'''


def number_of_subscribers(subreddit):
    '''A function to return total number of subscribers of a subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    response = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
