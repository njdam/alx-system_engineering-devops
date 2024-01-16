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

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return (subscribers_count)
    elif response.status_code == 302:
        print("Subreddit {} is a redirect.".format(subreddit))
        return (0)
    elif response.status_code == 404:
        print("Subreddit {} is not fount.".format(subreddit))
        return (0)
    else:
        # Handling other errors
        print(f"Error {response.status_code}: Unable to fetch data.")
        return (0)
