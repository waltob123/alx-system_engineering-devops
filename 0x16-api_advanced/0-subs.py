#!/usr/bin/python3
'''
0-subs - queries the Reddit API and returns the number
    of subscribers for a given subreddit.

Constraints:
1.  (not active users, total subscribers)

return 0 if an invalid subreddit is given.
'''

import requests
import sys


def number_of_subscribers(subreddit):
    '''
    Makes a request to reddit api and return number of subscribers

    Args:
        `subbredit (str)`: subreddit to get

    Return:
        `subscribers (int)`: number of subscribers to the subreddit
        `0`: if subbreddit is not valid
    '''
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '{}:0x16.api.advanced:v1 (by u/waltob123)'.format
               (sys.platform)}

    response = requests.get(url=url, headers=headers)

    # check if response is valid
    if response.status_code == 404:
        return 0
    subscribers = response.json().get('data').get('subscribers')
    return subscribers
