def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for char in number:
        if int(char) % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)
    return odd_sum, even_sum

number = input()
odd_sum, even_sum = odd_and_even_sum(number)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
