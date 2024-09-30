import FreeSimpleGUI as sg

if __name__ == "__main__":
    # Create a text label for task input
    input_label = sg.Text("Enter a task")
    # Create an input box for user to enter task
    input_box = sg.InputText()
    # Create a button to add the task
    add_button = sg.Button("Add")

    # Create the main window with a layout containing the input elements
    window = sg.Window("Todo List", layout=[[input_label, input_box, add_button]])

    # Display the window and wait for an event
    window.read()
    # Close the window when done
    window.close()
