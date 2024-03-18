def genrange(start_num, end_num):
    current_num = start_num
    while current_num <= end_num:
        yield current_num
        current_num += 1

print(list(genrange(1, 10)))