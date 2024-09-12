tasks = []
def show_menu():
    print("\nTo-Do List:")
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Mark a task as priority")
    print("4. Remove priority from a task")
    print("5. Group tasks")
    print("6. Show tasks")
    print("7. Exit")


def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "priority": False, "group": None})
    print(f"Task '{task}' added.")


def edit_task():
    show_tasks()
    task_num = int(input("Which task number do you want to edit? ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['task'] = input("Enter the updated task: ")
        print("Task updated.")
    else:
        print("Invalid task number.")

def mark_priority():
    show_tasks()
    task_num = int(input("Which task number to mark as priority? ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['priority'] = True
        print("Task marked as priority.")
    else:
        print("Invalid task number.")


def remove_priority():
    show_tasks()
    task_num = int(input("Which task number to remove priority from? ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['priority'] = False
        print("Priority removed from task.")
    else:
        print("Invalid task number.")


def group_tasks():
    show_tasks()
    task_num1 = int(input("Which task number to group with? ")) - 1
    task_num2 = int(input("Which task number to group? ")) - 1
    if 0 <= task_num1 < len(tasks) and 0 <= task_num2 < len(tasks):
        tasks[task_num1]['group'] = task_num2
        tasks[task_num2]['group'] = task_num1
        print("Tasks grouped.")
    else:
        print("Invalid task numbers.")


def show_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            priority = " (Priority)" if task['priority'] else ""
            group = f" (Grouped with {task['group'] + 1})" if task['group'] is not None else ""
            print(f"{i}. {task['task']}{priority}{group}")


def todo_list():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            edit_task()
        elif choice == '3':
            mark_priority()
        elif choice == '4':
            remove_priority()
        elif choice == '5':
            group_tasks()
        elif choice == '6':
            show_tasks()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


todo_list()