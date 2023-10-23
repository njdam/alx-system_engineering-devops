#!/usr/bin/python3
"""A Python script to, using this REST API, for a given employee ID."""

import requests
from sys import argv, exit


if __name__ == '__main__':
    # Checking number of arguments
    if len(argv) > 1:
        # Employee Id
        employee_id = argv[1]
        # Api url where to request information
        base_url = 'https://jsonplaceholder.typicode.com'

        # response user and todos by employee id
        user = requests.get(f'{base_url}/users/{employee_id}')
        todos = requests.get(f'{base_url}/todos?userId={employee_id}')

        # Checking status of requested employee id, failed to be fetched
        if user.status_code != 200 or todos.status_code != 200:
            print(f'Failed to fetch data for employee {employee_id}')
            exit(1)

        # User data into json file
        user_data = user.json()
        todos_data = todos.json()

        # Tasks completed
        tasks_completed = [todo for todo in todos_data if todo['completed']]
        total_tasks = len(todos_data)

        # Printing TODOs list progress of a given employ id
        print(f"Employee {user_data['name']} is done with tasks ", end="")
        print(f"({len(tasks_completed)}/{total_tasks}):")

        for task in tasks_completed:
            print(f"\t{task['title']}")
