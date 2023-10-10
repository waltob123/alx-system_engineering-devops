#!/usr/bin/python3
'''
2-recurse module
'''

import sys
import requests


def recurse(subreddit, after='', hot_list=[]):
    '''
    queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    If no results are found for the given subreddit, return None.
    '''

    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': '{}:0x16.api.advanced:v1 (by u/waltob123)'.format
               (sys.platform)}
    params = {'limit': 100, 'after': after}

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    results = response.json().get('data')
    after = results.get('after')
    for child in results.get('children'):
        hot_list.append(child.get('data').get('title'))

    if after is None:
        return hot_list
    return recurse(subreddit, after=after, hot_list=hot_list)
