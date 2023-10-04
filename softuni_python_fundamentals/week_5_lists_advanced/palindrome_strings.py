strings = list(input().split())
searched_palindrome = input()
palindromes = []

for string in strings:
    if string == "".join(reversed(string)):
        palindromes.append(string)

counter = palindromes.count(searched_palindrome)

print(palindromes)
print(f"Found palindrome {counter} times")
