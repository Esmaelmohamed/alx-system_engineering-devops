#!/usr/bin/python3
"""Export data from an API to JSON format."""
from json import dumps  # Import dumps function to serialize data to JSON
import requests  # Import requests module to make HTTP requests


def get_tasks_from_employee(response, employee):
    """Get all the tasks of an employee."""
    # Create a list to store all the tasks of the employee
    employee_tasks = []

    # Find the tasks that belong to this employee
    for task in response:
        if task.get('userId') == employee.get('id'):
            task_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }
            employee_tasks.append(task_data)

    # Return the list of tasks
    return employee_tasks


if __name__ == '__main__':
    # Main formatted names to API URIs and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    users_uri = '{api}/users'.format(api=api_url)
    todos_uri = '{api}/todos'.format(api=api_url)
    filename = 'todo_all_employees.json'

    # Users Response
    u_res = requests.get(users_uri).json()

    # Users TODO Response
    t_res = requests.get(todos_uri).json()

    # Dictionary to store all tasks of each employee
    users_tasks = {}

    # Store all tasks of each employee in the API data
    for user in u_res:
        user_id = user.get('id')

        # Get a list of all tasks of the current employee
        user_tasks = get_tasks_from_employee(t_res, {
            'id': user_id,
            'username': user.get('username')
        })

        # Store the list of all tasks of the current employee
        # in a dictionary that stores all employees with their tasks.
        users_tasks[user_id] = user_tasks

    # Create the new file with all the information
    # Filename example: `todo_all_employees.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(users_tasks))

