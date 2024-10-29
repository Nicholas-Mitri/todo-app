"""
Todo List Application - Web Version
Author: Nicholas Mitri
Date: 2024-10-29

A web-based version of the todo list application that allows users to manage their tasks
through a browser interface. Provides functionality to add, edit, complete and manage
to-do items via a web UI.
"""

import os
import streamlit as st

from main_opt import write_todos

st.header("My TODO App")


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

    for todo in todos:
        st.checkbox(todo)

    st.text_input(
        label="Add Task", placeholder="Add new task...", label_visibility="hidden"
    )

#     while True:

#         event, values = app_window.read()  # type: ignore
#         print(event)
#         print(values)

#         # Match the user action to the corresponding case
#         match event:
#             case "Add":
#                 # Add a new task to the todo list
#                 if not values["task"]:
#                     sg.popup("No task was entered. Please try again.")
#                     continue
#                 todos.append(values["task"] + "\n")
#                 write_todos(todos, path_to_todo)
#                 tasks_list.update(todos)

#             case "todos":
#                 todo_to_edit = values["todos"][0].rstrip("\n")
#                 input_box.update(value=todo_to_edit)

#             case "Edit":
#                 todo_to_edit = values["todos"][0]
#                 new_todo = values["task"] + "\n"
#                 if not new_todo:
#                     sg.popup("No task was entered. Please try again.")
#                     continue
#                 index = todos.index(todo_to_edit)
#                 todos[index] = new_todo
#                 write_todos(todos, path_to_todo)
#                 tasks_list.update(todos)

#             case "Complete":

#                 if len(values["todos"]) == 0:
#                     sg.popup("No task selected. Please try again.")
#                     continue
#                 todo_to_complete = values["todos"][0]
#                 index = todos.index(todo_to_complete)
#                 todos.pop(index)
#                 write_todos(todos, path_to_todo)
#                 tasks_list.update(todos)
#             case "Exit":
#                 break
#             case sg.WIN_CLOSED:
#                 # Exit the loop and end the program
#                 break

#     app_window.close()
