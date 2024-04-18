#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")
        sys.exit(1)

    # Define constants and fetch employee ID from command-line argument
    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    # Fetch TODO list data for the employee ID
    RESPONSE = requests.get(
        f"{URL}/users/{EMPLOYEE_ID}/todos", params={"_expand": "user"})
    data = RESPONSE.json()

    # Check if data is empty
    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    # Extract relevant information from the data
    TASK_TITLE = [task["title"] for task in data if task["completed"]]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)
    EMPLOYEE_NAME = data[0]["user"]["name"]

    # Print employee's TODO list progress
    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        # Print each completed task title
        print("\t", title)
