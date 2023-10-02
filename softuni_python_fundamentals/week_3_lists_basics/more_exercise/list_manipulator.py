numbers = list(int(x) for x in input().split(" "))
even = []
odd = []
new_list = []

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
    elif user_command == "max odd":
        if not odd:
            print("No matches")
            continue
        max_odd = max(odd)
        for i in range(len(numbers) - 1, - 1, - 1):
            if numbers[i] == max_odd:
                print(i)
                break
    elif user_command == "max even":
        if not even:
            print("No matches")
            continue
        max_even = max(even)
        for i in range(len(numbers) - 1, - 1, - 1):
            if max_even == numbers[i]:
                print(i)
                break
    elif user_command == "min even":
        if not even:
            print("No matches")
            continue
        min_even = min(even)
        for i in range(len(numbers) - 1, - 1, - 1):
            if numbers[i] == min_even:
                print(i)
                break
    elif user_command == "min odd":
        if not odd:
            print("No matches")
            continue
        min_odd = min(odd)
        for i in range(len(numbers) - 1, - 1, - 1):
            if numbers[i] == min_odd:
                print(i)
                break
    elif user_command[:5] == "first":
        new_list = []
        if user_command[8:] == "even":
            counter = int(user_command[6])
            if counter > len(numbers):
                print("Invalid count")
                continue
            for num in numbers:
                if num % 2 == 0:
                    new_list.append(num)
                    if counter == len(new_list):
                        break
        elif user_command[8:] == "odd":
            counter = int(user_command[6])
            if counter > len(numbers):
                print("Invalid count")
                continue
            for num in numbers:
                if num % 2 != 0:
                    new_list.append(num)
                    if counter == len(new_list):
                        break
        print(new_list)
    elif user_command[:4] == "last":
        new_list = []
        if user_command[7:] == "even":
            counter = int(user_command[5])
            if counter > len(numbers):
                print("Invalid count")
                continue
            for idx in range(len(numbers) - 1, -1, -1):
                if numbers[idx] % 2 == 0:
                    new_list.insert(0, numbers[idx])
                    if counter == len(new_list):
                        break
        elif user_command[7:] == "odd":
            counter = int(user_command[5])
            if counter > len(numbers):
                print("Invalid count")
                continue
            for idx in range(len(numbers) - 1, -1, -1):
                if numbers[idx] % 2 != 0:
                    new_list.insert(0, numbers[idx])
                    if counter == len(new_list):
                        break
        print(new_list)
    elif user_command == "end":
        print(numbers)
        break
