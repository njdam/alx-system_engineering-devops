#!/usr/bin/python3
"""A Python script to, using this REST API, for a given employee ID."""

import requests
from sys import argv, exit
import json


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

        # User data into json file
        user_data = user.json()
        todos_data = todos.json()
        # Json file where to store information of a given employee
        json_filename = f"{user_data['id']}.json"
        # List of task to be stored for a given employee
        task_list = []
        for task in todos_data:
            task_dict = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            }
            task_list.append(task_dict)

        # Data to export with user id and his/her list of tasks
        data_to_export = {user_data["id"]: task_list}

        # Writing data_to_export into json file
        with open(json_filename, 'w') as json_file:
            json.dump(data_to_export, json_file)
