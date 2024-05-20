#!/usr/bin/python3
'''fetches emloyee stuff'''
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "employee/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "tasks", params={"employee id": sys.argv[1]}).json()

    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]
