import streamlit as st
import funtions

todos = funtions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + '\n')
    funtions.set_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to incress your productivity.")
for todo in todos:
    st.checkbox(todo)
st.text_input(label="", placeholder="Add new Todo here",
              on_change=add_todo, key='new_todo')

