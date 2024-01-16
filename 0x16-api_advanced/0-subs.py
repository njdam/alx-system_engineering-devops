#!/usr/bin/python3
""" A function to querry Reddit API and return number of subscribers. """
import requests


def number_of_subscribers(subreddit):
    """ A function to return total number of subscribers of a subreddit. """
    # Reddit API to get subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Setting custom user agent to avoid many request errors
    headers = {'User-Agent': 'CustomUserAgent'}

    # Api request
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
