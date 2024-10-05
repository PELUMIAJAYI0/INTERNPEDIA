# A do to list app

#function to add tasks
def add_task():
    print("...Add Task...")
    number_of_task = int(input(f"{user_name}, how many tasks do you want to add---> "))

    for i in range(number_of_task):
        task_name = input("Enter the name of the task---> ")
        task = {"task": task_name, "done":False}
        tasks.append(task)
        print(f"Task--> {task_name} added successfully")

def list_all_task():
    print("...List All Tasks...")
    if not tasks:
        print("No tasks currently available")
    else:
        for index, task in enumerate(tasks):
            status = "done " if task['done'] else "not done"
            print(f"{index+1}. {task['task']} - {status}")

#function to mark task as done
def mark_task():
    print("...Mark Task as Done...")
    list_all_task()
    task_number = int(input("Enter the number of the task you want to mark as done--> "))
    if task_number > len(tasks):
        print("Invalid task number")
    else:
        tasks[task_number-1]['done'] = True
        print(f"Task--> {tasks[task_number-1]['task']} marked as done")

#function to delete task
def delete_task():
    print("...Delete Task...")
    list_all_task()
    task_number = int(input("Enter the number of the task you want to delete--> "))
    if task_number > len(tasks):
        print("Invalid task number")
    else:
        #tasks.pop(task_number-1)
        del tasks[task_number-1]
        print(f"Task--> {tasks[task_number-1]['task']} deleted successfully")

#function to exit app
def exit_app():
    print("...Exiting App...")
    print("Thanks for using the app")
    exit()
    
                      
    



#created an empty list to store the taaks
tasks = []
user_name = input("Enter your name---> ").capitalize()

print(f"Hello {user_name} Welcome to the to-do list app")
while True:
    print("\n1. Add task")
    print("2. List all task")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit App")

    user_choice = input("Enter your choice---> ")

    if user_choice == "1":
        add_task()
    elif user_choice == "2":
        list_all_task()
    elif user_choice == "3":
        mark_task()
    elif user_choice == "4":
        delete_task()
    elif user_choice == "5":
        exit_app()
    else:
        print("Invalid choice. Please try again")
    

