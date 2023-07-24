'''
#!/usr/bin/python3
""" Python script that uses [REST API](https://jsonplaceholder.typicode.com/),
    for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(i)) for i in completed]

'''
#!/usr/bin/python3
"""Script that uses REST API"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args).json()
        args = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args).json()
        todos_len = 0
        todos_arr = []
        for i in todos:
            if i.get("completed"):
                todos_arr.append(i)
                todos_len += 1

        print("Employee {} is done with tasks({}/{}):".format(
              users[0].get("name"), todos_len, len(todos)))

        for i in todos_arr:
            print("\t {}".format(i.get("title")))
