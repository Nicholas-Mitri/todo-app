"""
Todo List Application - Web Version
Author: Nicholas Mitri
Date: 2024-10-29

A web-based version of the todo list application that allows users to manage their tasks
through a browser interface. Provides functionality to add, edit, complete and manage
to-do items via a web UI.
"""

import os
import time
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


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    write_todos(todos, path_to_todo)
    message_placeholder.write(f"Success!!")
    st.session_state["new_todo"] = ""


def del_todo():
    for key, value in st.session_state.items():
        if key.startswith("chk"):  # type: ignore
            if value:
                break

    index = int(key[-1])  # type: ignore
    message_placeholder.write(f":material/check: {todos[index]}")
    todos.pop(index)
    write_todos(todos, path_to_todo)
    del st.session_state[key]


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

    for i, todo in enumerate(todos):
        st.checkbox(todo, on_change=del_todo, key=f"chk_{i}")

    st.text_input(
        label="Add Task",
        placeholder="Add new task...",
        label_visibility="hidden",
        on_change=add_todo,
        key="new_todo",
    )

    message_placeholder = st.empty()
