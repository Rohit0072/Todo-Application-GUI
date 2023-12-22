FILE_PATH = 'todos.txt'
def get_todos(filepath=FILE_PATH):
    """Read a text file and return
        the list of to-do item.
    """
    with open(filepath, 'r') as file_local:
        todos_local: list = file_local.readlines()
    return todos_local


def set_todos(todos_arg, filepath=FILE_PATH):
    """Write the to-do item list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
