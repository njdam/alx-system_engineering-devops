#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    """recursive function that queries the Reddit API."""
    URL = 'https://www.reddit.com'
    headers = {
            'Accept': 'application/json',
            'User-Agent': 'CustomUserAgent'
            }
    sort = 'hot'
    limit = 30

    response = requests.get(
            '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
                URL,
                subreddit,
                sort,
                limit,
                n,
                after if after else ''
                ),
            headers=headers,
            allow_redirects=False
            )

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        counts = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if counts >= limit and data['after']:
            return recurse(subreddit, hot_list, n + counts, data['after'])
        else:
            return hot_list if hot_list else None

    else:
        return hot_list if hot_list else None
