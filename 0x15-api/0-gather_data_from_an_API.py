#!/usr/bin/python3
"""
Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    # Check if an employee ID is provided and is a valid integer
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Base URL for the API
    api_url = 'https://jsonplaceholder.typicode.com'
    # URL for user information based on employee ID
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    # URL for user's TODO list
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    # Fetch user information
    res = requests.get(user_uri).json()

    # Get the name of the employee
    name = res.get('name')

    # Fetch the user's TODO list
    res = requests.get(todo_uri).json()

    # Total number of tasks
    total = len(res)

    # Number of non-completed tasks
    non_completed = sum([elem['completed'] is False for elem in res])

    # Number of completed tasks
    completed = total - non_completed

    # Print the summary of completed tasks
    output = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(output.format(emp_name=name, completed=completed, total=total))

    # Print each completed task title
    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))

