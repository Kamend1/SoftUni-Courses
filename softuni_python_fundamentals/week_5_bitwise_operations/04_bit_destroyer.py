def destroy_bit_at_position(number, position):
    mask = 1 << position
    mask = ~mask
    number = number & mask
    return number

user_number = int(input())
user_position = int(input())
print(destroy_bit_at_position(user_number, user_position))
