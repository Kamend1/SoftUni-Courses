from math import floor

n = int(input())
bit = input()
binary_string = ""
counter = 0

while n != 0:
    binary_string += str(n % 2)
    n = floor(n / 2)

binary_string = binary_string[::-1]

for i in range(len(binary_string)):
    if bit == binary_string[i]:
        counter += 1

print(counter)
