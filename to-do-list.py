def show_menu():
    print("TO-DO List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")


def remove_task(todo_list):
    if not todo_list:
        print("No tasks to remove.")
        return

    print("Current tasks:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def show_tasks(todo_list):
    if not todo_list:
        print("No tasks to show.")
    else:
        print("Current tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")


def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            show_tasks(todo_list)
        elif choice == "4":
            print("Exiting TO-DO list.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
