def even_odd(*args):
    even = []
    odd = []
    for num in args[:-1]:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if args[-1] == 'even':
        return even
    else:
        return odd
print(even_odd(1, 2, 3, 4, 5, 6, "even"))