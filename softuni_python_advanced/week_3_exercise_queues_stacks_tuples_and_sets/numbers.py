first_sequence = set(num for num in input().split())
second_sequence = set(num for num in input().split())
counter = int(input())

for _ in range(counter):
    command = input().split()
    first_command = command[0]
    if first_command == "Add":
        second_command = command[1]
        if second_command == "First":
            for num in command[2:]:
                first_sequence.add(num)
        elif second_command == "Second":
            for num in command[2:]:
                second_sequence.add(num)
    elif first_command == "Remove":
        second_command = command[1]
        if second_command == "First":
            for num in command[2:]:
                if num in first_sequence:
                    first_sequence.remove(num)
        elif second_command == "Second":
            for num in command[2:]:
                if num in second_sequence:
                    second_sequence.remove(num)
    elif first_command == "Check":
        print(second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence))

print(', '.join(sorted(first_sequence)))
print(', '.join(sorted(second_sequence)))
