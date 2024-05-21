#!/usr/bin/python3
'''exportin to JSON'''

import json
import sys
import urllib.request

if __name__ == "__main__":
    ID = sys.argv[1]

    data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/".format(
            ID))
    taks = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
            ID))

    data_dict = json.loads(employee_data.read().decode())
    tasks_dict = json.loads(taks.read().decode())

    task_done_count = 0
    total_tasks = 0
    completed_tasks = []
    for tasku in tasks_dict:
        if tasku["completed"] is True:
            completed_tasks.append(tasku)
            task_done_count += 1
        total_tasks += 1

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
            for task in tasks_dict  # completed_tasks
        ]
    }

    filename = "{}.json".format(USER_ID)
    with open(filename, mode="w") as file:
        json.dump(data, file)
