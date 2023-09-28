numbers = list(int(x) for x in input().split(" "))
even = []
odd = []

for element in numbers:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)

while True:
    user_command = input()
    if user_command[:8] == "exchange":
        idx = int(user_command[9:])
        if idx < 0 or idx >= len(numbers):
            print("Invalid index")
            continue
        numbers_1 = numbers[:idx + 1]
        numbers_2 = numbers[idx + 1:]
        numbers = numbers_2 + numbers_1
    if user_command == "max odd":
        if not odd:
            print("No matches")
            continue
        max_index = 0
        for i in range(len(odd)):
            if odd[i] >= odd[max_index]:
                max_index = i
        print(max_index)
    if user_command == "max even":
        if not even:
            print("No matches")
            continue
        max_index = 0
        for i in range(len(even)):
            if even[i] >= even[max_index]:
                max_index = i
        print(max_index)
    if user_command == "min even":
        if not even:
            print("No matches")
            continue
        min_index = 0
        for i in range(len(even)):
            if even[i] <= even[min_index]:
                min_index = i
        print(min_index)
    if user_command == "min odd":
        if not odd:
            print("No matches")
            continue
        min_index = 0
        for i in range(len(odd)):
            if odd[i] <= odd[min_index]:
                min_index = i
        print(min_index)
    if user_command[:5] == "first":
        if user_command[8:] == "even":
            idx = int(user_command[6])
            if idx >= len(even) or not even:
                print("Invalid count")
                continue
            new_list = even[:idx]
            print(new_list)
        elif user_command[8:] == "odd":
            idx = int(user_command[6])
            if idx >= len(odd) or not odd:
                print("Invalid count")
                continue
            new_list = odd[:idx]
            print(new_list)
    if user_command[:4] == "last":
        if user_command[7:] == "even":
            idx = int(user_command[5])
            if idx >= len(even) or not even:
                print("Invalid count")
                continue
            new_list = even[idx:]
            print(new_list)
        elif user_command[7:] == "odd":
            idx = int(user_command[5])
            if idx >= len(odd) or not odd:
                print("Invalid count")
                continue
            new_list = odd[idx:]
            print(new_list)

    if user_command == "end":
        print(numbers)
        break
