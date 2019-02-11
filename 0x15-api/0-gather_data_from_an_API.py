#!/usr/bin/python3
""" request todo list """

import requests
from sys import argv


if __name__ == "__main__" and len(argv) > 1:

    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            argv[1])
    try:
        print("Employee {} ".format(response.json().pop("name")), end='')
    except KeyError:
        quit()

    task_list = []
    todos = 0
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    for x in response.json():
        if x.get("userId") is int(argv[1]):
            if x.get("completed") is True:
                task_list.append(x.get("title"))
            todos += 1
    print("is done with tasks({}/{}):\n\t {}".format(
          len(task_list), todos, "\n\t ".join(task_list)))
