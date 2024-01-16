#!/usr/bin/python3
"""A recursive function that queries the Reddit API."""

import requests


def sort_histogram(histogram={}):
    """A function to sorts and prints a given histogram.
    """
    histogram = list(filter(lambda key: key[1], histogram))
    histo_dict = {}
    for item in histogram:
        if item[0] in histo_dict:
            histo_dict[item[0]] += item[1]
        else:
            histo_dict[item[0]] = item[1]

    histogram = list(histo_dict.items())
    histogram.sort(key=lambda key: key[0], reverse=False)
    histogram.sort(key=lambda key: key[1], reverse=True)

    results = '\n'.join(list(map(
        lambda key: f'{key[0]}: {key[1]}', histogram
        )))

    if results:
        print(results)


def count_words(subreddit, word_list, histogram=[], n=0, after=None):
    """Counts number  of times each word in a given wordlist.
    """
    URL = 'https://www.reddit.com'
    api_headers = {
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
            headers=api_headers,
            allow_redirects=False
            )

    if not histogram:
        word_list = list(map(lambda word: word.lower(), word_list))
        histogram = list(map(lambda word: (word, 0), word_list))

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        titles = list(map(lambda post: post['data']['title'], posts))
        histogram = list(map(
            lambda key: (key[0], key[1] + sum(list(map(
                lambda txt: txt.lower().split().count(key[0]),
                titles
                )))),
            histogram
            ))
        if len(posts) >= limit and data['after']:
            count_words(
                    subreddit,
                    word_list,
                    histogram,
                    n + len(posts),
                    data['after']
                    )
        else:
            sort_histogram(histogram)
    else:
        return
