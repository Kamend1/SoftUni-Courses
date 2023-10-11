def invert_bits(number, position):
    mask = 7 << position  # 7 is 111 in binary, the three bits to be inverted
    inverted_bits = number ^ mask
    return inverted_bits

user_number = int(input())
user_position = int(input())

result = invert_bits(user_number, user_position)
print(result)
