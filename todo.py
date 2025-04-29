import sys
import os

# sys: Lets you read command-line arguments like add, list, done, etc.
# os: Helps with file checking and file system operations (like checking if the tasks file exists)

TASKS_FILE = 'tasks.txt'
# This is the filename where all your tasks will be saved. It's just a regular text file.

# ------------------------------
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Checks if tasks.txt exists.
# If it doesn't, return an empty list.
# If it does, read each line, remove the newline (\n), and return the list of tasks.

# ------------------------------
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:  # FIXED: 'w' must be lowercase, not 'W'
        for task in tasks:
            file.write(task + '\n')

# Takes a list of tasks and writes them back to tasks.txt.
# Each task is written on a new line.

# ------------------------------
def add_task(task_text):  # FIXED: name should be add_task not add_tasks (to match main)
    tasks = load_tasks()
    tasks.append(f"[ ] {task_text}")  # Add checkbox formatting
    save_tasks(tasks)
    print(f'Added task: {task_text}')

# ------------------------------
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):  # FIXED: show tasks one-by-one, numbered from 1
        print(f"{i}. {task}")

# ------------------------------
def mark_done(task_index):
    tasks = load_tasks()  # FIXED: was load_task() — typo
    index = task_index - 1  # FIXED: changed variable name from task_number to task_index
    if 0 <= index < len(tasks):
        tasks[index] = tasks[index].replace("[ ]", "[x]", 1)  # Only replace first match
        save_tasks(tasks)
        print(f'Marked task {task_index} as done.')
    else:
        print(f'Invalid task number: {task_index}')

# ------------------------------
def delete_task(task_num):
    tasks = load_tasks()
    index = task_num - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f'Deleted task: {removed}')
    else:
        print("Invalid task number.")

# ------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add/list/done/delete")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        task_text = " ".join(sys.argv[2:])
        add_task(task_text)
    elif command == "list":
        list_tasks()
    elif command == "done":
        mark_done(int(sys.argv[2]))
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    else:
        print("Unknown command.")
