import os
import FreeSimpleGUI as sg

from main_opt import write_todos


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

    with open(path_to_todo, "r") as file:
        todos = file.readlines()

    # Create a text label for task input
    input_label = sg.Text("Enter a task")
    # Create an input box for user to enter task
    input_box = sg.InputText(tooltip="Enter a task", key="task")
    # Create a button to add the task
    add_button = sg.Button("Add", tooltip="Add a new task to the list")
    # Create a button to edit the task
    edit_button = sg.Button("Edit", tooltip="Edit an existing task")
    # Create a button to add the task
    complete_button = sg.Button("Complete", tooltip="Mark selected task as complete")
    # Create list of tasks
    tasks_list = sg.Listbox(
        values=todos,
        key="todos",
        enable_events=True,
        size=[45, 10],
    )
    # Create the main window with a layout containing the input elements
    app_window = sg.Window(
        "Todo List",
        layout=[
            [input_label],
            [input_box, add_button],
            [tasks_list, [edit_button], [complete_button]],
        ],
        font=("helvetica", 20),
    )

    while True:

        event, values = app_window.read()  # type: ignore
        print(event)
        print(values)

        # Match the user action to the corresponding case
        match event:
            case "Add":
                # Add a new task to the todo list
                if not values["task"]:
                    sg.popup("No task was entered. Please try again.")
                    continue
                todos.append(values["task"] + "\n")
                write_todos(todos, path_to_todo)
                tasks_list.update(todos)

            case "todos":
                todo_to_edit = values["todos"][0].rstrip("\n")
                input_box.update(value=todo_to_edit)

            case "Edit":

                todo_to_edit = values["todos"][0]
                new_todo = values["task"] + "\n"
                if not new_todo:
                    sg.popup("No task was entered. Please try again.")
                    continue
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos, path_to_todo)
                tasks_list.update(todos)

            case "Complete":

                if len(values["todos"]) == 0:
                    sg.popup("No task selected. Please try again.")
                    continue
                todo_to_complete = values["todos"][0]
                index = todos.index(todo_to_complete)
                todos.pop(index)
                write_todos(todos, path_to_todo)
                tasks_list.update(todos)

            case sg.WIN_CLOSED:
                # Exit the loop and end the program
                break

    app_window.close()
