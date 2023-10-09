elements_list = list(input().split())
moves_counter = 0

while True:
    user_command = input()
    if user_command == 'end':
        print("Sorry you lose :(")
        print(*elements_list, sep=' ')
        break
    moves_counter += 1
    user_command_list = user_command.split()
    start_idx = int(user_command_list[0])
    end_idx = int(user_command_list[1])
    if start_idx == end_idx:
        print("Invalid input! Adding additional elements to the board")
        middle_idx = len(elements_list) // 2
        elements_list.insert(middle_idx, f"-{moves_counter}a")
        elements_list.insert(middle_idx, f"-{moves_counter}a")
        continue
    if start_idx < 0 or end_idx < 0 or start_idx >= len(elements_list) or end_idx >= len(elements_list):
        print("Invalid input! Adding additional elements to the board")
        middle_idx = len(elements_list) // 2
        elements_list.insert(middle_idx, f"-{moves_counter}a")
        elements_list.insert(middle_idx, f"-{moves_counter}a")
        continue
    first_element = elements_list[start_idx]
    second_element = elements_list[end_idx]
    if first_element == second_element:
        print(f"Congrats! You have found matching elements - {first_element}!")
        elements_list.remove(first_element)
        elements_list.remove(second_element)
        if len(elements_list) == 0:
            print(f"You have won in {moves_counter} turns!")
            break
    elif first_element != second_element:
        print("Try again!")
    user_command_list.clear()
