n = int(input())
numbers = []
filtered = []

for num in range(n):
    num = int(input())
    numbers.append(num)


command = input()

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered.append(num)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered.append(num)
elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered.append(num)

print(filtered)
