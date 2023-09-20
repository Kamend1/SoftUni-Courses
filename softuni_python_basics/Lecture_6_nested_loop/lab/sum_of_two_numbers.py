first_number = int(input())
second_number = int(input())
magic_number = int(input())
total_counter = 0
success_counter = 0

for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        total_counter += 1
        if success_counter == 1:
            break
        if i + j - magic_number == 0:
            success_counter += 1
            print(f"Combination N:{total_counter} ({i} + {j} = {magic_number})")

if success_counter == 0:
    print(f"{total_counter} combinations - neither equals {magic_number}")
