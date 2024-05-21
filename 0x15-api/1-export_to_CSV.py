#!/usr/bin/python3
'''exportin prv data to csv'''
import sys
import requests
import re


url = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(url, id)).json()
            tasks = requests.get('{}/todos'.format(url)).json()
            names = user.get('username')
            tobd = list(filter(lambda x: x.get('userId') == id, tasks))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in tobd:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            names,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
