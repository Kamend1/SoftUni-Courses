set_even = set()
set_odd = set()

for i in range(1, int(input()) + 1):
    name_score = sum(ord(char) for char in input()) // i

    if name_score % 2 == 0:
        set_even.add(name_score)
    else:
        set_odd.add(name_score)

if sum(set_even) == sum(set_odd):
    set_union = set_odd.union(set_even)
    print(*set_union, sep=', ')
elif sum(set_even) < sum(set_odd):
    set_difference = set_odd.difference(set_even)
    print(*set_difference, sep=', ')
else:
    set_sym_difference = set_odd.symmetric_difference(set_even)
    print(*set_sym_difference, sep=", ")
