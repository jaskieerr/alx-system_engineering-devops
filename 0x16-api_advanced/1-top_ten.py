#!/usr/bin/python3
'''Top Ten'''

import requests


def top_ten(subreddit):
    ''' prints titles of first 10 hot posts listed for a subreddit'''
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    res = requests.get(api_url, headers={'User-agent': 'Oluwabunmi Olabode'},
                        allow_redirects=False)
    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        count = 0
        for post in posts:
            if count == 10:
                break
            print(post.get("data").get("title"))
            count = count + 1
    else:
        print("None")
