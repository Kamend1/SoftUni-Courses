number = int(input())

for i in range(0, number +1):
    print(" " * (number - i) + "*" * i + " " + chr(124) + " " + "*" * i)
