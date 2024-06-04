#!/usr/bin/python3
"""Module for recursively fetching all hot posts of a subreddit"""

import requests

def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Recursively queries the Reddit API to retrieve all hot posts of a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot posts.
        count (int): Number of posts retrieved so far.
        after (str): The fullname of the last post in the previous request.

    Returns:
        list: A list of titles of all hot posts, or None if the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-user-agent-for-subreddit-query"}
    params = {"count": count, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list += [child.get("data", {}).get("title", "No Title") for child in children]

        after = data.get("after")
        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, count + len(children), after)
    except requests.RequestException:
        return None

