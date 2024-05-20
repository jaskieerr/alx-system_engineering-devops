#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    try:
        employee = requests.get(url + "users/{}".format(employee_id)).json()
        username = employee.get("username")
        tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

        with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
            fieldnames = ["Employee ID", "Username", "Completed", "Task Title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow({
                    "Employee ID": employee_id,
                    "Username": username,
                    "Completed": task.get("completed"),
                    "Task Title": task.get("title")
                })
        print("CSV export successful.")
    except requests.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)

