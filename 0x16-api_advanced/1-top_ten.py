#!/usr/bin/python3
"""
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """print the titles of the top 10 hottest post on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "muri"}
    params = {"limit": 10}
    response = get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
