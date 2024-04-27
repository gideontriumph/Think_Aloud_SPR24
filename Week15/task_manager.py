"""
    Name: task_manager.py
    Author: Triumph Ogbonnia
    Created: 4/26/24
    Purpose: Task manager 
"""

import json
import random
import re
import hashlib
import logging

logging.basicConfig(level=logging.INFO)

# Define global variables
users_file = "users.json"
tasks_file = "tasks.json"

# Function to load user data from file
def load_users():
    try:
        with open(users_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning("Users file not found. Creating new one.")
        return {}

# Function to save user data to file
def save_users(users):
    try:
        with open(users_file, "w") as file:
            json.dump(users, file)
    except Exception as e:
        logging.error(f"Error saving users: {e}")

# Function to load task data from file
def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning("Tasks file not found. Creating new one.")
        return []

# Function to save task data to file
def save_tasks(tasks):
    try:
        with open(tasks_file, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")

# Function for user registration
def register_user(username, password):
    users = load_users()
    if username in users:
        print("\nUsername already exists. Please choose another one.")
        return
    if not is_valid_username(username):
        print("\nInvalid username. Username should only contain alphanumeric characters and underscores.")
        return
    if not is_valid_password(password):
        print("\nInvalid password. Password should be at least 8 characters long.")
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = {"password": hashed_password, "tasks": []}
    save_users(users)
    print("\nUser registered successfully.")

# Function for user login
def login_user(username, password):
    users = load_users()
    if username not in users or users[username]["password"] != hashlib.sha256(password.encode()).hexdigest():
        print("Invalid username or password.")
        return None
    print("Login successful.")
    return username

# Function to add a new task
def add_task(username, task_name, due_date):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "name": task_name, "due_date": due_date})
    save_tasks(tasks)
    users = load_users()
    users[username]["tasks"].append(task_id)
    save_users(users)
    print("Task added successfully.")

# Function to display user's tasks
def display_tasks(username):
    tasks = load_tasks()
    users = load_users()
    user_tasks = users[username]["tasks"]
    print("\nYour Tasks:")
    for task_id in user_tasks:
        task = next((task for task in tasks if task["id"] == task_id), None)
        if task:
            print(f"Task ID: {task['id']}\nName: {task['name']}\nDue Date: {task['due_date']}\n------------------------")
        else:
            print(f"Task with ID {task_id} not found.")
    if not user_tasks:
        print("You have no tasks.")

    if user_tasks:
        print("\nOptions:")
        print("1. Delete Task")
        print("2. Back")
        option = input("Enter option: ")
        if option == "1":
            task_id_to_delete = input("Enter task ID to delete: ")
            delete_task(username, int(task_id_to_delete))

# Function to delete a task
def delete_task(username, task_id):
    tasks = load_tasks()
    users = load_users()
    user_tasks = users[username]["tasks"]
    if task_id not in user_tasks:
        print("Task not found.")
        return
    user_tasks.remove(task_id)
    save_users(users)
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("\nTask deleted successfully.")

# Function to generate random tasks for demonstration
def generate_random_tasks():
    tasks = []
    for i in range(10):
        task_name = f"Task {i+1}"
        due_date = f"2024-04-{random.randint(1, 30)}"
        tasks.append({"id": i+1, "name": task_name, "due_date": due_date})
    return tasks

# Function to validate username
def is_valid_username(username):
    return bool(re.match("^[a-zA-Z0-9_]+$", username))

# Function to validate password
def is_valid_password(password):
    return len(password) >= 8

# Main function
def main():
    print("*** Welcome to the Task Manager! ***")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if user:
                while True:
                    print("\n1. Add Task\n2. View Tasks\n3. Logout")
                    user_choice = input("\nEnter your choice: ")
                    if user_choice == "1":
                        task_name = input("\nEnter task name: ")
                        due_date = input("Enter due date (YYYY-MM-DD): ")
                        add_task(username, task_name, due_date)
                    elif user_choice == "2":
                        display_tasks(username)
                    elif user_choice == "3":
                        print("\nLogged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()