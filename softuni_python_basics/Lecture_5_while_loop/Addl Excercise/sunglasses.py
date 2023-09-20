number = int(input())

print("*" * number * 2 + " " * number + "*" * number * 2)
for i in range(number - 2):
    if i == int((number - 1) / 2 -1):
        print("*" + "/" * (2 * number - 2) + "*" + chr(124) * number + "*" + "/" * (2 * number - 2) + "*")
    else:
        print("*" + "/" * (2 * number - 2) + "*" + " " * number + "*" + "/" * (2 * number - 2) + "*")
print("*" * number * 2 + " " * number + "*" * number * 2)
