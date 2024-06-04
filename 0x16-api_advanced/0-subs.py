#!/usr/bin/python3
"""Module to fetch the number of subscribers of a subreddit"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-user-agent-for-subreddit-query"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0

