#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests
headers = {"User-Agent": "Mozilla/5.0"}


def recurse(subreddit, hot_list=[], after=None):
    """query the Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
          .format(subreddit, after)
    article = requests.get(url, headers=headers, allow_redirects=False)

    if article.status_code == 200:
        for children in article.json().get("data").get("children"):
            hot_list.append(children.get("data").get("title"))

        after = article.json().get("data").get("after")
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)

    else:
        return None
