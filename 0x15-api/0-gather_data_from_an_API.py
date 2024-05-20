#!/usr/bin/python3
'''fetches employee stuff'''
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in tasks if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]
