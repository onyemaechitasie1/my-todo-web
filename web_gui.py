import streamlit as st
import main_function

lst = main_function.get_todos()

0
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    lst.append(new_todo)
    main_function.write_todos(lst)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app increases your productivity")

for index, todo in enumerate(lst):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        lst.pop(index)
        main_function.write_todos(lst)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add a todo", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")