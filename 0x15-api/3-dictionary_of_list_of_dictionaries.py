#!/usr/bin/python3
"""A Python script to, using this REST API, for a given employee ID."""

import json
import requests


if __name__ == '__main__':
    # Api url where to request information
    base_url = 'https://jsonplaceholder.typicode.com'

    # response user and todos by employee id
    users = requests.get(f'{base_url}/users')
    todos = requests.get(f'{base_url}/todos')

    # User data into json file
    users_data = users.json()
    todos_data = todos.json()

    # List of task to be stored by each user
    tasks_by_user = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        tasks_by_user[user_id] = []

    for task in todos_data:
        user_id = task['userId']
        # Finding a username of a provided task in all tasks by at task 0
        username = [user['username'] for user in users_data if (
            user['id'] == user_id)][0]

        task_dict = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
                }
        tasks_by_user[user_id].append(task_dict)
        # Json file where to store information of a given employee
        json_filename = "todo_all_employees.json"

        # Writing tasks by each user into single json file
        with open(json_filename, 'w') as json_file:
            json.dump(tasks_by_user, json_file)
