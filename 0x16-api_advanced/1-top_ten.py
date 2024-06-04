#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16)'}
    response = requests.get(url, headers=headers)

    try:
        top_posts = response.json().get('data', {}).get('children', [])
        for post in top_posts:
            print(post.get('data', {}).get('title'))
    except KeyError:
        print("None")

