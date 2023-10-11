def bit_at_position(number):
    shifted_number = number >> 1
    lsb = shifted_number & 1
    return lsb

user_number = int(input())
print(bit_at_position(user_number))
