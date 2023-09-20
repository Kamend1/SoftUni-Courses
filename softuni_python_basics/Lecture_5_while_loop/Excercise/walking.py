daily_target_steps = 10000
total_steps_done = 0

while total_steps_done < daily_target_steps:
    user_input_command = input()
    if user_input_command == "Going home":
        numer_steps_home = int(input())
        total_steps_done += numer_steps_home
        difference = abs(daily_target_steps - total_steps_done)
        if total_steps_done >= daily_target_steps:
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
            break
        else:
            print(f"{difference} more steps to reach goal.")
            break
    else:
        total_steps_done += int(user_input_command)
else:
    difference = abs(daily_target_steps - total_steps_done)
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
