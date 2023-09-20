key = int(input())
lines = int(input())

for i in range(lines):
    letter = input()
    char = chr(ord(letter) + key)
    print(char, end="")
