import json
FILE_NAME="tasks.json"
def load_tasks():
    try:
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_tasks():
    with open(FILE_NAME,'w')as file:
        json.dump(tasks,file,indent=4)    
def add_task():
    task=input("Enter an Task:- ")
    tasks.append({
        "title":task,
        "completed":False
    })
    save_tasks()
    print("Task Added Sucessfully")
def view_task():
    if len(tasks)==0:
        print("No task")
        return
    for i,task in enumerate(tasks,start=1):
        if task["completed"]:
            status="completed"
        else:
            status="Pending"
        print(f"{i}.{task['title']} [{status}]")
def complete_task():
    if len(tasks)==0:
        return
    n=int(input("Enter the task nnumber to complete:- "))
    if 1 <= n <=len(tasks):
        tasks[n-1]['completed']=True
        save_tasks()
        print("Task Completed")
    else:
        print("Invalid task number")
def delete_task():
    if len(tasks)==0:
        return
    n=int(input("Enter task number to delete:- ")) 
    if 1<=n<=len(tasks):
        deleted=tasks.pop(n-1)
        save_tasks()
        print(f"Deleted Task: {deleted['title']}")
    else:
        print("Invalid Task number")
def main():

    while True:

        print("\n==============================")
        print("      STUDENT TASK MANAGER")
        print("==============================")

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_task()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
tasks=load_tasks()
main()
           


