#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of total subscribers for the subreddit.
    """
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    
    subscriber_count = response.json().get('data', {}).get('subscribers', 0)
    return subscriber_count

