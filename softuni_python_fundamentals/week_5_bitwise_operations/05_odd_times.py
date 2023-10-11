def xor_for_a_list(list):
    result = 0
    for number in list:
        result ^= number
    return result

numbers = [int(x) for x in input().split()]
print(xor_for_a_list(numbers))
