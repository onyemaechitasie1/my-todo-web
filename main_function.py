def get_todos(filepath='lst.txt'):
    """ get_todos is a function that get todos from
    filepath lst.txt"""
    with open(filepath, 'r') as file_functions:
        lst_function = file_functions.readlines()
        return lst_function


def write_todos(get_lst, filepath='lst.txt'):
    with open(filepath, 'w') as file_function:
        file_function.writelines(get_lst)


#excluding main_function from running in main.py, use conditional
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
