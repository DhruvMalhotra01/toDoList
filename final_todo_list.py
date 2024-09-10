tasks = []

def show_menu():
    print("\nTo-Do list:")
    print("PRESS '1' TO ADD TASK")
    print("PRESS '2' TO EDIT TASK")
    print("PRESS '3' TO MARK AS PRIORITY")
    print("PRESS '4' TO DELETE TASK")
    print("PRESS '5' TO GROUP TASK")
    print("PRESS '6' TO SHOW TASKS")
    print("PRESS '7' TO EXIT LIST")

def add_task():

def edit_task():

def mark_as_task():

def delete_task():




    def todo_list():
        while True:
            show_menu()
            entered_value = input("Choose an option between 1 to 7")
            if entered_value == "1":
                add_task()
            elif entered_value == "2":
                edit_task()
            elif entered_value == "3":
                mark_as_priority()
            elif entered_value == "4":
                delete_task()
            elif entered_value == "5":
                group_task()
            elif entered_value == "6":
                show_tasks()
            elif entered_value == "7":
                print("Thanks for use!!!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 7")

todo_list()
