#!/usr/bin/python3
""" reddit api request module """

import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Cheese Pizza'})
session.allow_redirects = False
url = "https://www.reddit.com/"


def number_of_subscribers(subreddit):
    """ fetches number of subscribers """
    reddit = session.get(url + 'r/' + subreddit + '/about.json')
    if reddit.json().get("kind") != "t5":
        return 0
    return reddit.json().get("data").get("subscribers")


def top_ten(subreddit):
    """ fetches top ten hot posts in a subreddit """
    reddit = session.get(url + 'r/' + subreddit + '/hot.json',
                         params={"limit": "10"})
    titles = []
    for x in reddit.json().pop("data").pop("children"):
        titles.append(x.pop("data").pop("title"))
    print("\n".join(titles) or None)
