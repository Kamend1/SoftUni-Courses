chat_list = []
user_command = input().split()

while user_command[0] != "end":
    if user_command[0] == "Chat":
        chat_list.append(user_command[1])
    elif user_command[0] == "Delete":
        if user_command[1] in chat_list:
            chat_list.remove(user_command[1])
    elif user_command[0] == "Edit":
        if user_command[1] in chat_list:
            index = chat_list.index(user_command[1])
            chat_list[index] = user_command[2]
    elif user_command[0] == "Pin":
        if user_command[1] in chat_list:
            index = chat_list.index(user_command[1])
            chat_list.pop(index)
            chat_list.append(user_command[1])
    elif user_command[0] == "Spam":
        for message in user_command[1:]:
            chat_list.append(message)
    user_command = input().split()

for message in chat_list:
    print(message)
