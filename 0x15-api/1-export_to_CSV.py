#!/usr/bin/python3
"""Python REST API"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    try:
        if len(argv) < 2 or type(eval(argv[1])) is not int:
            exit(1)

            uid = argv[1]
            url = 'https://jsonplaceholder.typicode.com'

            todo_url = "{}/todos?userId={}".format(url, uid)
            user_url = "{}/users/{}".format(url, uid)

            # get user's name
            user = requests.get(user_url)
            user_name = user.json().get("usernname")

            # get task done by user
            todo = requests.get(todo_url)
            with open('{}.csv'.format(uid), 'x', encoding="utf-8") as f:
                writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                for attr in todo.json():
                    writer.writerow([argv[1], user_name, attr.get('completed'),
                                    attr.get('title')])
    except Exception:
        exit

