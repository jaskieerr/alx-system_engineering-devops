#!/usr/bin/python3
'''
How many subs?
'''
import requests


def number_of_subscribers(subreddit):
    ''''checks how many subs'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'testu'})
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
