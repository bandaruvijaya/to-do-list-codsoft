# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to delte a task from the list
def delete_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

# Function to display all tasks
def display_tasks():
    if tasks:
        print("\n*** To-Do List ***")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the to-do list.")

# Main program loop
while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    
    elif choice == '2':
        display_tasks()
        task_index = int(input("Enter task index to delete (1-based): ")) - 1
        delete_task(task_index)
    
    elif choice == '3':
        display_tasks()
    
    elif choice == '4':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")