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


def recurse(subreddit, hot_list=[]):
    """ fetches all hot posts in a subreddit recursively """
    reddit = session.get(url + 'r/' + subreddit + '/hot.json')
    for x in reddit.json().get("data").get("children"):
        hot_list.append(x.pop("data").pop("title"))
    more = reddit.json().get("data").pop("after")
    if more:
        session.params = {"after": more}
        return(recurse(subreddit, hot_list))
    else:
        return hot_list or None


def count_words(subreddit, word_list=[]):
    """ fetches all hot posts in a subreddit recursively """
    if type(word_list) is not dict:
        word_list = {x: 0 for x in word_list}
    reddit = session.get(url + 'r/' + subreddit + '/hot.json')
    titles = []
    for x in reddit.json().get("data").get("children"):
        titles.extend(x.get("data").get("title").split())
    for word in word_list.keys():
        for title in titles:
            clean = ''.join(x for x in title if x.isalnum())
            if word.lower() == clean.lower():
                word_list[word] += 1
    more = reddit.json().get("data").pop("after")
    if more:
        session.params = {"after": more}
        count_words(subreddit, word_list)
    else:
        for x in sorted(word_list.items(), key=lambda x: x[1], reverse=True):
            if x[1] > 0:
                print("{}: {}".format(x[0], x[1]))
