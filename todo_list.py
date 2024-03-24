
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Mark Item as Completed")
    print("4. Remove Item from To-Do List")
    print("5. Exit")


def view_todo_list(todo_list):
    print("To-Do List:")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")


def add_item(todo_list):
    item = input("Enter the task you want to add: ")
    todo_list.append(item)
    print("Task added to the to-do list.")


def mark_completed(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        todo_list[index] += " (Completed)"
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid index.")


def remove_item(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to remove: ")) - 1
        del todo_list[index]
        print("Task removed from the to-do list.")
    except (IndexError, ValueError):
        print("Invalid index.")


def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_item(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            remove_item(todo_list)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()