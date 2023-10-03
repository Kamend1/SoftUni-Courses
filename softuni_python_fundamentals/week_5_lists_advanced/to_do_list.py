notes = [0] * 10

while True:
    user_command = input()
    if user_command == "End":
        break
    list_user_command = user_command.split("-")
    importance = int(list_user_command[0]) - 1
    task = list_user_command[1]
    notes.pop(importance)
    notes.insert(importance, task)

result = [element for element in notes if element != 0]
print(result)
