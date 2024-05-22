#!/usr/bin/python3
"""Export data from an API to CSV format."""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Check if the argument can be converted to a number
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted names to API URIs and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # Fetch user information
    res = requests.get(user_uri).json()

    # Get the username of the employee
    username = res.get('username')

    # Fetch user's TODO list
    res = requests.get(todo_uri).json()

    # Create the new file for the user to save the information
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        # Write the CSV header
        writer.writerow(['Employee ID', 'Username', 'Completed', 'Title'])

        # Write each task to the CSV file
        for elem in res:
            # Task completion status
            status = elem.get('completed')

            # Task title
            title = elem.get('title')

            # Write each task as a row in the CSV file
            writer.writerow([emp_id, username, status, title])

