# It is a ToDo App that helps you manage your  efficiently.

# The application is a console application that allows the user to add, show, edit, complete and exit tasks.

import os
from re import S
from datetime import datetime

print("Today is", datetime.now().strftime("%b %d, %Y"))


def write_file(todos, path_to_todo):
    """
    Write the list of todos to a file.

    Args:
        'todos' (list): A list of todo items to be written to the file.
        path_to_todo (str): The file path where the todos will be saved.

    This function opens the specified file in write mode and writes all
    the todo items from the 'todos' list to the file.
    """
    with open(path_to_todo, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":

    # Initialize an empty list to store todo items
    todos = []
    # Set the path for the todo file using os.path.join for cross-platform compatibility
    path_to_todo = os.path.join(os.curdir, "files", "todos.txt")

    # Check if the directory of the given path exists
    if not os.path.exists(os.path.dirname(path_to_todo)):
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(path_to_todo), exist_ok=True)

    # Continuously prompt the user for an action
    while True:
        # Read the todo list from the file
        with open(path_to_todo, "r") as file:
            todos = file.readlines()

        # Prompt the user for an action and normalize the input
        user_action = (
            input("Type (a)dd, (s)how, (e)dit, (c)omplete, or (q)uit: ").strip().lower()
        )
        # Check if the user entered any input
        if len(user_action) == 0:
            print("No input was entered. Please try again.")
            continue

        # Match the user action to the corresponding case
        match user_action.split()[0]:
            case "add" | "a":
                # Add a new task to the todo list
                if len(user_action.split()) == 1:
                    print("No task was entered. Please try again.")
                    continue
                todo = user_action.split()[1] + "\n"
                with open(path_to_todo, "a") as file:
                    file.write(todo)

            case "show" | "s":
                # Show all tasks in the todo list
                if os.path.exists(path_to_todo) and len(todos) > 0:
                    for index, item in enumerate(todos, start=1):
                        print(f"{index}: {item}", end="")
                else:
                    print("No tasks found.")

            case "edit" | "e":
                # check if the task list exists
                if os.path.exists(path_to_todo):
                    if len(user_action.split()) < 3:
                        print(
                            "Invalid input. Use format (e)dit <NUM> <NEW TASK>. Please try again."
                        )
                        continue
                    else:
                        # Edit an existing task in the todo list
                        try:
                            number = int(user_action.split()[1])
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

                        new_todo = user_action.split()[2] + "\n"
                        todos[number - 1] = new_todo
                        write_file(todos, path_to_todo)
                else:
                    print("No tasks found.")

            case "complete" | "c":
                # Mark a task as complete and remove it from the todo list
                if os.path.exists(path_to_todo):
                    if len(user_action.split()) < 2:
                        print(
                            "Invalid input. Use format (c)omplete <NUM>. Please try again."
                        )
                        continue
                    else:
                        try:
                            number = int(user_action.split()[1])
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
                    removed_todo = todos.pop(number - 1)
                    write_file(todos, path_to_todo)
                    print(f"Completed: {removed_todo}")
                else:
                    print("No tasks found.")

            case "quit" | "q":
                # Exit the loop and end the program
                break

            case "help" | "h":
                # Display available commands to the user
                print(
                    "Available commands:\n"
                    "(a)dd: Add a new task to the todo list.\n"
                    "\tFormat: (a)dd <TASK>\n"
                    "(s)how: Show all tasks in the todo list.\n"
                    "\tFormat: (s)how\n"
                    "(e)dit: Edit an existing task in the todo list.\n"
                    "\tFormat: (e)dit <NUM> <NEW TASK>\n"
                    "(c)omplete: Mark a task as complete and remove it from the todo list.\n"
                    "\tFormat: (c)omplete <NUM>\n"
                    "(h)elp: Show the available commands.\n"
                    "quit: Exit the program.\n"
                )

            case _:
                print("Invalid input. Please try again.")


# Create a decorator that will log the time a function takes to execute.
