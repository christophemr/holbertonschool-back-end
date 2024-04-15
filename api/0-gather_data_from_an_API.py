#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URL for fetching employee's TODO list
    url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Send GET request to fetch TODO list data
        response = requests.get(url)

        # Raise an exception for non-2xx status codes
        response.raise_for_status()

        # Convert response JSON to Python data
        todo_data = response.json()
        return todo_data
    except requests.RequestException as e:
        # Handle request errors
        print("Error fetching data:", e)
        return None


def display_todo_progress(todo_data):
    if not todo_data:
        return

    # Assuming employee name is the same as userID (first task's userId)
    employee_name = todo_data[0]["userId"]

    # Total number of tasks
    total_tasks = len(todo_data)

    # Number of completed tasks
    completed_tasks = sum(task["completed"] for task in todo_data)

    # Titles of completed tasks
    completed_task_titles = [task["title"]
                             for task in todo_data if task["completed"]]

    # Display progress information
    print(
        f"Employee {employee_name} is done with tasks
        ({completed_tasks}/{total_tasks}): "
    )
    for title in completed_task_titles:
        # Print each completed task title with tabulation
        print("\t", title)


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(f"Usage: python {__file__} employee_id(int)")
        sys.exit(1)

    # Extract employee ID from command-line argument
    employee_id = sys.argv[1]

    # Fetch employee's TODO list progress
    todo_data = get_employee_todo_progress(employee_id)

    # Display progress information if data is fetched successfully
    if todo_data:
        display_todo_progress(todo_data)


if __name__ == "__main__":
    main()
