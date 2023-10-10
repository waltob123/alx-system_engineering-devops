#!/usr/bin/python3
'''
100-count - queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
'''

import sys
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    '''
    Prints counts of given words found in hot posts of a given subreddit.
    '''

    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': '{}:0x16.api.advanced:v1 (by u/waltob123)'.format
               (sys.platform)}
    params = {'after': after, 'count': count, 'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print('')
        return

    results = results.get('data')
    after = results.get('after')
    count += results.get('dist')
    for c in results.get('children'):
        title = c.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print('')
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print('{}: {}'.format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
