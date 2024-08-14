#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress """
import requests
from sys import argv

if __name__ == "__main__":
    """ main code """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url+'users/'+argv[1]).json()
    todos_response = requests.get(url+'todos?userId='+argv[1]).json()
    completed_todos = requests.get(url+'todos?userId='+argv[1] + 
                                   '&completed=true').json()
    num_of_done = len(completed_todos)
    total_num = len(todos_response)
    user_name = user_response.get("name")
    print("Employee {} is done with tasks({}/{}):"
    .format(user_name, num_of_done, total_num))
    for i in completed_todos:
        print('\t {}'.format(i.get('title')))
