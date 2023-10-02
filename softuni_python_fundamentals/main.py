numbers = list(int(x) for x in input().split(" "))
user_command = input()

if user_command[:5] == "first":
    if user_command[8:] == "even":
        counter = int(user_command[6])
        if counter >= len(numbers):
            print("Invalid count")

        for num in numbers:
            new_list = []
            if counter == 0:
                break
            if num % 2 == 0:
                counter -= 1
                new_list.append(num)
        print(new_list)
    elif user_command[8:] == "odd":
        counter = int(user_command[6])
        if counter >= len(numbers):
            print("Invalid count")

        for num in numbers:

            if counter == 0:
                break
            if num % 2 != 0:
                counter -= 1
                new_list.append(num)
        print(new_list)
