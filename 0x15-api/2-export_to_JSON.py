#!/usr/bin/python3
""" requests all task list for user and exports to json file """

import requests
from sys import argv
import json


if __name__ == "__main__" and len(argv) > 1:

    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            argv[1])
    try:
        name = response.json().pop("username")
    except KeyError:
        quit()

    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user = {argv[1]: []}
    for x in response.json():
        if x.get("userId") is int(argv[1]):
            user[argv[1]].append({"task": x.get("title"),
                                  "completed": x.get("completed"),
                                  "username": name})
    with open(argv[1] + ".json", 'w') as jfile:
        json.dump(user, jfile)
