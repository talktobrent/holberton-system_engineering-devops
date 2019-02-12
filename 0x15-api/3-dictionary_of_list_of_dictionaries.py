#!/usr/bin/python3
""" requests all task list for user and exports to json file """

import json
import requests


if __name__ == "__main__":

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = response.json()
    user_dict = {}
    task_list = []
    for user in users:
        for task in list(tasks):
            if task.get("userId") == user.get("id"):
                task_list.append({"username": user.get("username"),
                                  "task": task.get("title"),
                                  "completed": task.get("completed")})
                tasks.remove(task)
        user_dict.update({user.get("id"): task_list})
        task_list = []

    with open("todo_all_employees.json", 'w') as jfile:
        json.dump(user_dict, jfile)
