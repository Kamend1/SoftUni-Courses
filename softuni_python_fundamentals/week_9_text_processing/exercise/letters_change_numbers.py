strings = input().split()
results = []

for string in strings:
    digit_string = ""
    result = 0
    string = string.strip()
    for char in string:
        if char.isdigit():
            digit_string += char
    digit = int(digit_string)
    if string[0].isupper():
        operator = ord(string[0]) - ord("A") + 1
        result = digit / operator
    else:
        operator = ord(string[0]) - ord("a") + 1
        result = digit * operator
    if string[-1].isupper():
        operator = ord(string[-1]) - ord("A") + 1
        result -= operator
    else:
        operator = ord(string[-1]) - ord("a") + 1
        result += operator
    results.append(result)

print(f"{sum(results):.2f}")
