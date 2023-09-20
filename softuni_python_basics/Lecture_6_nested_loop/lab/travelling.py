user_command = input()

while user_command != "End":
    destination_budget = float(input())
    while destination_budget > 0:
        saved_amount = float(input())
        destination_budget -= saved_amount
    else:
        print(f"Going to {user_command}!")
    user_command = input()
