#my first solution
#
# first_sequence = set(int(num) for num in input().split())
# second_sequence = set(int(num) for num in input().split())
# counter = int(input())
#
# for _ in range(counter):
#     first_command, second_command, *data = input().split()
#     if first_command == "Add":
#         if second_command == "First":
#             [first_sequence.add(int(num)) for num in data]
#         elif second_command == "Second":
#             [second_sequence.add(int(num)) for num in data]
#     elif first_command == "Remove":
#         if second_command == "First":
#             [first_sequence.discard(int(num)) for num in data]
#         elif second_command == "Second":
#             [second_sequence.discard(int(num)) for num in data]
#     else:
#         print(second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence))
#
# print(*sorted(first_sequence), sep=", ")
# print(*sorted(second_sequence), sep=", ")

# Solution by SoftUni lecturer
first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())

functions = {
    "Add First": lambda x: [first_sequence.add(int(num)) for num in x],
    "Add Second": lambda x: [second_sequence.add(int(num)) for num in x],
    "Remove First": lambda x: [first_sequence.discard(int(num)) for num in x],
    "Remove Second": lambda x: [second_sequence.discard(int(num)) for num in x],
    "Check Subset": lambda x: print(second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence)),
}


for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + ' ' + second_command

    functions[command](data)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
