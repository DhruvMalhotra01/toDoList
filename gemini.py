def show_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append({"task": task, "priority": False})  # Create a dictionary
    print("Task added.")

def edit_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[index] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def mark_priority(tasks):
    show_tasks(tasks)
    index = int(input("Enter the task number to mark as priority: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["priority"] = True
        print("Task marked as priority.")
    else:
        print("Invalid task number.")


def remove_priority(tasks):
    show_tasks(tasks)
    index = int(input("Enter the task number to remove priority from: ")) - 1
    if 0 <= index < len(tasks):
        print("Priority removed from task.")
        tasks[index]["priority"] = False
    else:
        print("Invalid task number.")



def todo_list():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            edit_task(tasks)
        elif choice == '3':
            mark_priority(tasks)
        elif choice == '4':
            remove_priority(tasks)
        
        elif choice == '5':
            show_tasks(tasks)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

def show_menu():
    print("\nTo-Do List:")
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Mark a task as priority")
    print("4. Remove priority from a task")
    print("5. Group tasks")
    print("6. Show tashks")
    print("7. Exit")

todo_list()