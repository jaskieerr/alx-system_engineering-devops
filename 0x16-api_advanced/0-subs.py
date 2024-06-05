#!/usr/bin/python3
'''
How many subs?
'''
import requests


def number_of_subscribers(subreddit):
    ''''cheks how many subs'''
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(api_url, headers={'User-agent': 'Oluwabunmi Olabode'})
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
