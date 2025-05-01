import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import datetime

TASKS_FILE = 'tasks_gui.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()
    for task in tasks:
        color = "black"
        if "[x]" in task:
            color = "green"
        elif "High" in task:
            color = "red"
        elif "Medium" in task:
            color = "orange"
        elif "Low" in task:
            color = "blue"
        task_listbox.insert(tk.END, task)
        task_listbox.itemconfig(tk.END, {'fg': color})

def add_task():
    task = task_entry.get().strip()
    due = due_entry.get().strip()
    priority = priority_var.get()

    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return

    task_text = f"[ ] {task} | Due: {due if due else 'None'} | Priority: {priority}"
    tasks = load_tasks()
    tasks.append(task_text)
    save_tasks(tasks)
    task_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    refresh_task_list()

def delete_task():
    selection = task_listbox.curselection()
    if not selection:
        messagebox.showwarning("Selection Error", "Select a task to delete.")
        return
    index = selection[0]
    tasks = load_tasks()
    removed = tasks.pop(index)
    save_tasks(tasks)
    refresh_task_list()
    messagebox.showinfo("Deleted", f"Deleted: {removed}")

def mark_done():
    selection = task_listbox.curselection()
    if not selection:
        messagebox.showwarning("Selection Error", "Select a task to mark as done.")
        return
    index = selection[0]
    tasks = load_tasks()
    if "[ ]" in tasks[index]:
        tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
    save_tasks(tasks)
    refresh_task_list()

# ----- GUI Setup -----
app = tk.Tk()
app.title("📝 To-Do List (GUI)")
app.geometry("600x400")

# ----- Entry Fields -----
tk.Label(app, text="Task").grid(row=0, column=0, sticky="w", padx=5, pady=5)
task_entry = tk.Entry(app, width=40)
task_entry.grid(row=0, column=1, columnspan=3, sticky="we", padx=5)

tk.Label(app, text="Due Date (YYYY-MM-DD)").grid(row=1, column=0, sticky="w", padx=5)
due_entry = tk.Entry(app, width=20)
due_entry.grid(row=1, column=1, sticky="w")

tk.Label(app, text="Priority").grid(row=1, column=2, sticky="e")
priority_var = tk.StringVar()
priority_menu = ttk.Combobox(app, textvariable=priority_var, values=["Low", "Medium", "High"], width=10)
priority_menu.grid(row=1, column=3)
priority_menu.set("Medium")

# ----- Buttons -----
tk.Button(app, text="Add Task", command=add_task).grid(row=2, column=0, padx=5, pady=10)
tk.Button(app, text="Delete Task", command=delete_task).grid(row=2, column=1, padx=5)
tk.Button(app, text="Mark as Done", command=mark_done).grid(row=2, column=2, padx=5)
tk.Button(app, text="Exit", command=app.quit).grid(row=2, column=3, padx=5)

# ----- Task List -----
task_listbox = tk.Listbox(app, height=15, font=("Courier", 10))
task_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Allow resizing
app.grid_rowconfigure(3, weight=1)
app.grid_columnconfigure((0, 1, 2, 3), weight=1)

refresh_task_list()
app.mainloop()
