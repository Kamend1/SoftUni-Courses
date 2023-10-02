def tribonacci_calc(n):
    trib0 = 1
    trib1 = 1
    trib2 = 2
    result = 0
    if n == 1:
        previous_sequence = [1]
    elif n == 2:
        previous_sequence = [1, 1]
    elif n == 3:
        previous_sequence = [1, 1, 2]
    else:
        previous_sequence = [1, 1, 2]
        while len(previous_sequence) < n:
            result = trib0 + trib1 + trib2
            previous_sequence.append(result)
            trib0 = trib1
            trib1 = trib2
            trib2 = result

    return previous_sequence

n = int(input())
tribonacci_list = tribonacci_calc(n)
print(*tribonacci_list, sep=" ")
