number_cars = int(input())
train_car_list = []
for i in range(number_cars):
    train_car_list.append(0)

while True:
    user_command = input()
    list_user_command = user_command.split()
    if list_user_command[0] == "add":
        train_car_list[-1] += int(list_user_command[1])
    elif list_user_command[0] == "insert":
        train_car_list[int(list_user_command[1])] += int(list_user_command[2])
    elif list_user_command[0] == "leave":
        train_car_list[int(list_user_command[1])] -= (int(list_user_command[2]))
    if user_command == "End":
        break

print(train_car_list)
