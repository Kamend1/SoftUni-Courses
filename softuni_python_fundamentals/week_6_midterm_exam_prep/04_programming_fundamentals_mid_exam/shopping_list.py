shopping_list = input().split("!")

user_command = input().split()

while user_command[0] != "Go":
    if user_command[0] == "Urgent":
        if user_command[1] not in shopping_list:
            shopping_list.insert(0, user_command[1])
    elif user_command[0] == "Unnecessary":
        if user_command[1] in shopping_list:
            shopping_list.remove(user_command[1])
    elif user_command[0] == "Correct":
        if user_command[1] in shopping_list:
            index = shopping_list.index(user_command[1])
            shopping_list[index] = user_command[2]
    elif user_command[0] == "Rearrange":
        if user_command[1] in shopping_list:
            shopping_list.remove(user_command[1])
            shopping_list.append(user_command[1])

    user_command = input().split()

print(", ".join(shopping_list))
