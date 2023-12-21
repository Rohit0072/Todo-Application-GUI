from funtions import get_todos, set_todos
import time

now = time.strftime("%b %d, %y %M:%S")
print("Current Time is : ", now)

while True:
    # Getting User Value and strip space chars form it
    user_action = input("Type add, show, edit, complete or exit -:")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        set_todos()

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}--{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo : ")
            todos[number] = new_todo + '\n'

            set_todos()
            
        except ValueError:
            print("Your command is not vaild.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            set_todos()
            print(f"Todo '{todo_to_remove}' was removed from the list")
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not vaild.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not Valid.")

print("Bye!")
