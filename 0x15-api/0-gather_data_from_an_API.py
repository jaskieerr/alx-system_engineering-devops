#!/usr/bin/python3
'''fetches data from jasonsomethying'''

import json
import sys
import urllib.request

if __name__ == "__main__":
    ID = sys.argv[1]

    data = urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/users/{}/".format(
                ID))
    tasks = urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
                ID))

    data_dict = json.loads(data.read().decode())
    tasks_dict = json.loads(tasks.read().decode())

    tasks_done = 0
    all_tasks = 0
    done_list = []
    for tasku in tasks_dict:
        if tasku["completed"] is True:
            done_list.append(tasku)
            tasks_done += 1
        all_tasks += 1

    EMPLOYEE_NAME = data_dict["name"]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        tasks_done,
        all_tasks))

    for tasku in done_list:
        print("\t {}".format(tasku["title"]))
