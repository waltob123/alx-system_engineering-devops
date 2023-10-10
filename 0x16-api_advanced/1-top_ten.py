#!/usr/bin/python3
'''
1-top_ten module - queries the Reddit API and returns the title of
    the first 10 hot posts.
'''

import sys
import requests


def top_ten(subreddit):
    '''
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    '''

    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': '{}:0x16.api.advanced:v1 (by u/waltob123)'.format
               (sys.platform)}
    params = {'limit': 10}

    response = requests.get(url=url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print('None')
        return None
    results = response.json().get('data')
    [print(result.get('data').get('title')) for result in
     results.get('children')]
