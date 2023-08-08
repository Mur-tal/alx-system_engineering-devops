#!/usr/bin/python3
"""
    function that queries the Reddit API and returns the number of subscribers
"""
import requests
headers = {"User-Agent": "muri"}


def number_of_subscribers(subreddit):
    """return total subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub = requests.get(url, headers=headers, allow_redirects=False)

    if sub.status_code == 200:
        return sub.json().get("data").get("subscribers")

    return 0
