#!/usr/bin/python3
"""Top Ten file script by advanced api of reddit api."""

import requests


def top_ten(subreddit):
    """A function to return titles of the first 10 hot posts listed."""

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'UserAgent': 'CustomUserAgent'}
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
        else:
            print("No posts found in the subreddit.")

    elif response.status_code == 302:
        print(f"Subreddit '{subreddit}' is redirect."
                + "Please provide a valid subreddit.")

    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")

    else:
        print(f"Error {response.status_code}: Unable to fetch data.")
