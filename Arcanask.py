import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    task_text = input("🆕 Task description: ")
    due_date = input("📅 Due date (optional - YYYY-MM-DD): ")
    priority = input("⭐ Priority (High/Medium/Low): ").capitalize()

    full_task = f"[ ] {task_text} | Due: {due_date if due_date else 'None'} | Priority: {priority}"
    tasks = load_tasks()
    tasks.append(full_task)
    save_tasks(tasks)
    print(Fore.GREEN + f"✅ Task added: {task_text}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "📭 No tasks found.")
        return

    print(Fore.CYAN + "\n📋 Your Tasks:\n")
    for i, task in enumerate(tasks, 1):
        color = Fore.WHITE
        if "[x]" in task:
            color = Fore.GREEN
        elif "High" in task:
            color = Fore.RED
        elif "Medium" in task:
            color = Fore.YELLOW
        elif "Low" in task:
            color = Fore.BLUE

        print(color + f"{i}. {task}")

def task_summary():
    tasks = load_tasks()
    done = sum(1 for task in tasks if "[x]" in task)
    total = len(tasks)
    pending = total - done
    print(Fore.MAGENTA + f"\n📊 Summary: {done} done | {pending} pending | {total} total")

def mark_done():
    list_tasks()
    try:
        index = int(input("✔️ Task number to mark as done: ")) - 1
        tasks = load_tasks()
        if 0 <= index < len(tasks):
            tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            print(Fore.GREEN + f"✅ Task {index+1} marked as done.")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def delete_task():
    list_tasks()
    try:
        index = int(input("❌ Task number to delete: ")) - 1
        tasks = load_tasks()
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(Fore.RED + f"🗑️ Deleted: {removed}")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def main():
    while True:
        print("\n" + "="*50)
        print(Fore.CYAN + "📝  TO-DO LIST MENU".center(50))
        print("="*50)
        print("1️⃣  Add Task")
        print("2️⃣  List Tasks")
        print("3️⃣  Mark Task as Done")
        print("4️⃣  Delete Task")
        print("5️⃣  Task Summary")
        print("6️⃣  Exit")
        print("="*50)

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            task_summary()
        elif choice == '6':
            print(Fore.BLUE + "👋 Goodbye! Stay productive!")
            break
        else:
            print(Fore.RED + "⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
