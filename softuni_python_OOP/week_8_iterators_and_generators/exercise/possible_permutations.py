import itertools
from itertools import permutations

def possible_permutations(my_list):
    permutations = itertools.permutations(my_list, len(my_list))
    yeild = permutations

[print(n) for n in possible_permutations([1, 2, 3])]

