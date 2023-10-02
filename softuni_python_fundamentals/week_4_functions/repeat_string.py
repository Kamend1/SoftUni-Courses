string = input()
counter = int(input())

repeated_string = lambda a, b: a * b
new_string = repeated_string(string, counter)

print(new_string)
