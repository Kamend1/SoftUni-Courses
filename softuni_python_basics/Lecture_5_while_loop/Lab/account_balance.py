user_command_input = input()
total_sum = 0

while user_command_input != "NoMoreMoney":
    if float(user_command_input) <= 0:
        print("Invalid operation!")
        break
    else:
     total_sum += float(user_command_input)
     print(f"Increase: {float(user_command_input):.2f}")
     user_command_input = input()

print(f"Total: {total_sum:.2f}")
