# Student Task Manager

A simple task management application built using Python. The application allows users to add, view, complete, and delete tasks. Tasks are stored in a JSON file so that they can be saved and accessed even after the program is closed.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Store tasks using JSON
* Load previously saved tasks when the application starts
* Simple command-line interface

## Technologies Used

* Python
* JSON
* File Handling

## Project Structure

```text
student_task/
│
├── app.py
├── tasks.json
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/santoshrathnaam/student_task.git
```

### 2. Navigate to the project folder

```bash
cd student_task
```

### 3. Run the application

```bash
python app.py
```

## How It Works

When the application starts, it loads existing tasks from `tasks.json`.

The user can choose from the following options:

```text
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
```

Whenever a task is added, completed, or deleted, the updated task list is saved back to `tasks.json`.

## Example

```text
==============================
      STUDENT TASK MANAGER
==============================

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter your choice: 1
Enter a Task: Study Python

Task Added Successfully
```

## Future Improvements

* Add task editing
* Add task priorities
* Add due dates
* Add task search
* Add a graphical user interface
* Replace JSON storage with SQLite
* Convert the application into a web application

## Author

**Santosh Rathnaam S**

A beginner Python project created to practice Python programming, functions, data structures, file handling, and JSON.
