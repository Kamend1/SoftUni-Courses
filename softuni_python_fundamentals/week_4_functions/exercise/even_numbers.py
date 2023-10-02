def even_numbers(my_list):
    even_filtered = filter(lambda x: x % 2 == 0, my_list)
    return list(even_filtered)

my_list = [int(x) for x in input().split()]
even_numbers = even_numbers(my_list)
print(even_numbers)
