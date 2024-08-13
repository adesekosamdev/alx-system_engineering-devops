#!/usr/bin/python3
"""
Queries the Reddit API to return the number of subscribers for a given subreddit.

This function will return the total number of subscribers (not active users).
If an invalid subreddit is given, the function will return 0.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a given subreddit.
    
    This function will return the total number of subscribers (not active users).
    If an invalid subreddit is given, the function will return 0.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"}, # Custom User-Agent to avoid request restrictions
    )

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
