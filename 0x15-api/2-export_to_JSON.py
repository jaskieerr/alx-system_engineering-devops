#!/usr/bin/python3
'''Exporting to JSON'''

import json
import sys
import urllib.request

if __name__ == "__main__":
    ID = sys.argv[1]

    employee_data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(ID))
    tasks = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(ID))

    data_dict = json.loads(employee_data.read().decode())
    tasks_dict = json.loads(tasks.read().decode())

    EMPLOYEE_NAME = data_dict["name"]
    USERNAME = data_dict["username"]
    USER_ID = data_dict["id"]

    data = {
        USER_ID: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": USERNAME
            }
            for task in tasks_dict
        ]
    }

    filename = "{}.json".format(USER_ID)
    with open(filename, mode="w") as file:
        json.dump(data, file)
