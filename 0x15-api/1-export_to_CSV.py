#!/usr/bin/python3
""" requests all task list for user and exports to csv file """

import requests
from sys import argv
import csv


if __name__ == "__main__" and len(argv) > 1:

    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            argv[1])
    try:
        name = response.json().pop("name")
    except KeyError:
        quit()

    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    with open(argv[1] + ".csv", 'w') as csvfile:
        task = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for x in response.json():
            if x.get("userId") is int(argv[1]):
                task.writerow([argv[1], name, str(x.get("completed")),
                              x.get("title")])
