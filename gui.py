import funtions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightBrown1")

clock = sg.Text('', key="clock", font=("arial", 10))
label = sg.Text("Type in a to-do", font=("fantacy", 14))
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add",tooltip="Add button")
list_box = sg.Listbox(values=funtions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button =sg.Button("Edit")
complete_button = sg.Button("Complete",tooltip="To Complete Task")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvertica', 12))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = funtions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            funtions.set_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = funtions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                funtions.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Arial", 12))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = funtions.get_todos()
                todos.remove(todo_to_complete)
                funtions.set_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first!", font=("Arial", 12))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
