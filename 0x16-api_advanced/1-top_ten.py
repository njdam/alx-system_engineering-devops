#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a given subreddit.
    '''
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'CustomUserAgent'
    }
    sort = 'top'
    limit = 10
    response = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
