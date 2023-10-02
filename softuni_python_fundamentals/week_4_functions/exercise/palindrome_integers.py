def is_palindrome(number):
    is_palindrome = True
    for idx in range(len(number)):
        if number[idx] != number[-(idx + 1)]:
            is_palindrome = False
    if is_palindrome:
        print("True")
    else:
        print("False")

numbers = list(input().split(", "))

for number in numbers:
    is_palindrome(number)
