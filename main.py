# This is a project from the Udemy course "Python Mega Course", app 1.
# It is a ToDo App that helps you manage your  efficiently.

# The application is a console application that allows the user to add, show, edit, complete and exit tasks.

import os


if __name__ == "__main__":

    todos = []
    path_to_todo = os.path.join(os.curdir, "files", "todos.txt")

    # Check if the directory of the given path exists
    if not os.path.exists(os.path.dirname(path_to_todo)):
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(path_to_todo))

    # Infinite loop to continuously prompt the user for an action
    while True:
        # Prompt the user for an action and normalize the input
        user_action = (
            input("Type (a)dd, (s)how, (e)dit, (c)omplete, or (q)uit: ").strip().lower()
        )

        # Match the user action to the corresponding case
        match user_action:
            case "add" | "a":
                # Add a new task to the todo list
                todo = input("Enter a task: ") + "\n"
                with open(path_to_todo, "a") as file:
                    file.write(todo)

            case "show" | "s":
                # Show all tasks in the todo list
                if os.path.exists(path_to_todo):
                    with open(path_to_todo, "r") as file:
                        todos = file.readlines()
                    for index, item in enumerate(todos, start=1):
                        print(f"{index}: {item}", end="")
                else:
                    print("No tasks found.")

            case "edit" | "e":
                # Edit an existing task in the todo list
                if os.path.exists(path_to_todo):
                    with open(path_to_todo, "r+") as file:
                        todos = file.readlines()
                    try:
                        number = int(
                            input("Enter the number of the task you want to edit: ")
                        )
                        if not 1 <= number <= len(todos):
                            print(
                                f"Invalid input. Number between 1 and {len(todos)} expected."
                            )
                            continue
                    except ValueError:
                        print(
                            f"Invalid input. Number between 1 and {len(todos)} expected."
                        )
                        continue
                    new_todo = input("Enter the new task: ") + "\n"
                    todos[number - 1] = new_todo
                    with open(path_to_todo, "w") as file:
                        file.writelines(todos)
                else:
                    print("No tasks found.")

            case "c omplete" | "c":
                # Mark a task as complete and remove it from the todo list
                if os.path.exists(path_to_todo):
                    with open(path_to_todo, "r+") as file:
                        todos = file.readlines()
                    try:
                        number = int(
                            input("Enter the number of the task you want to complete: ")
                        )
                        if not 1 <= number <= len(todos):
                            print(
                                f"Invalid input. Number between 1 and {len(todos)} expected."
                            )
                            continue
                    except ValueError:
                        print(
                            f"Invalid input. Number between 1 and {len(todos)} expected."
                        )
                        continue
                    todos.pop(number - 1)
                    with open(path_to_todo, "w") as file:
                        file.writelines(todos)
                else:
                    print("No tasks found.")

            case "quit" | "q":
                # Exit the loop and end the program
                break

            case _:
                # Handle invalid input
                print("Invalid input. Please try again.")
