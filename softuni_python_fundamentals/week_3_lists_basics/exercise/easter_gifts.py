gift_list = list(input().split(" "))

while True:
    user_command = input()
    if user_command == "No Money":
        break
    list_command = list(user_command.split(" "))
    if list_command[0] == "OutOfStock":
        for i in range(len(gift_list)):
            if list_command[1] == gift_list[i]:
                gift_list[i] = None
    elif list_command[0] == "Required":
        if 0 < int(list_command[2]) < len(gift_list):
            gift_list[int(list_command[2])] = list_command[1]
    elif list_command[0] == "JustInCase":
        for i in range(len(gift_list) - 1, -1, -1):
            if gift_list[i] is None:
                continue
            else:
                gift_list[-1] = list_command[1]
                break
        else:
            gift_list[-1] = list_command[1]


for i in range(len(gift_list)):
    if gift_list[i] is None:
        continue
    else:
        print(gift_list[i], end=" ")
