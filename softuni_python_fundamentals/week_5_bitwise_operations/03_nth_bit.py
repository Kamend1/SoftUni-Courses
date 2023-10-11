def bit_at_position(number, position):
    shifted_number = number >> position
    lsb = shifted_number & 1
    return lsb

user_number = int(input())
user_position = int(input())
print(bit_at_position(user_number, user_position))
