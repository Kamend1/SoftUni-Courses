first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())
counter = int(input())

for _ in range(counter):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for num in command[2:len(command)]:
                first_sequence.add(int(num))
        elif command[1] == "Second":
            for num in command[2:len(command)]:
                second_sequence.add(int(num))
    elif command[0] == "Remove":
        if command[1] == "First":
            for num in command[2:len(command)]:
                if int(num) in first_sequence:
                    first_sequence.remove(int(num))
        elif command[1] == "Second":
            for num in command[2:len(command)]:
                if int(num) in second_sequence:
                    second_sequence.remove(int(num))
    else:
        print(second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
