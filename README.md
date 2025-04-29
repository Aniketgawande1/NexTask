

# ✅ Advanced CLI To-Do App 🧠📋

A feature-rich **command-line To-Do application** built with Python! Organize your tasks, manage due dates, authenticate users, and stay productive — all from your terminal.

---

## 🛠️ Built With

- 🐍 Python 3.x
- 🗃️ SQLite (or JSON for simple storage)
- 🔐 JWT (for optional authentication)
- 📦 Rich (for pretty CLI UI — optional)

---

## ✨ Features

- 👤 User registration & login
- 📝 Add, edit, delete tasks
- ⏰ Set and modify due dates
- ✅ Mark tasks as complete
- 🔍 Filter tasks (all / completed / pending)
- 📊 View tasks sorted by date or status
- 💾 Save data locally (file or SQLite)

---

## 🖥️ Usage

### 🚀 Run the App

```bash
python todo.py
```

### 🧩 Example Commands (Interactive CLI)

```bash
> login
> register
> add "Submit assignment" --due "2025-05-02"
> list --status "pending"
> complete 3
> delete 4
> logout
```

---

## 📁 Project Structure

```
cli-todo-app/
├── todo.py                 # Main CLI script
├── auth.py                 # Handles login/register/JWT
├── tasks.py                # Add/edit/delete task functions
├── database.py             # SQLite or file-based DB logic
├── utils.py                # Helper functions
└── README.md
```

---

## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/Aniketgawande1/cli-todo-app.git
cd cli-todo-app
```

2. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

3. Run:

```bash
python todo.py
```

---

## 🛡️ License

MIT License © 2025 [Aniket Gawande](https://github.com/Aniketgawande1)

---

Would you like me to generate this as a file for you or include support for a future React frontend too?
