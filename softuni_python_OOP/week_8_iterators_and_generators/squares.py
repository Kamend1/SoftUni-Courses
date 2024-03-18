def squares(num):
    current_num = 1
    while current_num <= num:
        yield current_num ** 2
        current_num = current_num + 1

print(list(squares(5)))