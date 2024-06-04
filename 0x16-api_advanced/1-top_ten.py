#!/usr/bin/python3
"""Module for fetching the top 10 hot posts of a subreddit"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to retrieve the top 10 hot posts of a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        None: Prints the titles of the top 10 hot posts, or 'None' if the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom-user-agent-for-subreddit-query"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print('None')
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print('None')
            return

        for post in posts:
            print(post.get("data", {}).get("title", "None"))
    except requests.RequestException:
        print('None')

