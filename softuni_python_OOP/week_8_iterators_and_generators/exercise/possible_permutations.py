from itertools import permutations

def possible_permutations(my_list):
    for el in permutations(my_list):
        yield list(el)

[print(n) for n in possible_permutations([1, 2, 3])]

