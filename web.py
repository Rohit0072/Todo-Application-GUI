import streamlit as st
import funtions

todos = funtions.get_todos()
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to incress your productivity.")
for todo in todos:
    st.checkbox(todo)
st.text_input(label="", placeholder="Add new Todo here")

