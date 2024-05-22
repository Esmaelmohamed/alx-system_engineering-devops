#!/usr/bin/python3
"""Export data from an API to JSON format."""
from json import dumps  # Importing dumps function to serialize data to JSON
import requests  # Importing requests module to make HTTP requests
from sys import argv  # Importing argv to access command-line arguments

if __name__ == '__main__':
    # Check if the argument can be converted to a number
    try:
        emp_id = int(argv[1])  # Extracting employee ID from command-line argument
    except ValueError:
        exit()  # Exit if argument cannot be converted to a number

    # Main formatted names to API URIs and filenames
    api_url = 'https://jsonplaceholder.typicode.com'  # Base URL for API
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)  # URL for user information based on employee ID
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)  # URL for user's TODO list
    filename = '{emp_id}.json'.format(emp_id=emp_id)  # Filename for JSON file, e.g., `1.json`

    # Fetch user information
    u_res = requests.get(user_uri).json()

    # Fetch user's TODO list
    t_res = requests.get(todo_uri).json()

    # List to store all tasks of a user
    user_tasks = []

    # Iterate over each task and collect relevant data
    for elem in t_res:
        data = {
            'task': elem.get('title'),  # Task title
            'completed': elem.get('completed'),  # Completion status of task
            'username': u_res.get('username')  # Username of the employee
        }

        user_tasks.append(data)  # Add task data to the list

    # Create a new JSON file to save the information
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))  # Write JSON data to the file, with employee ID as key

