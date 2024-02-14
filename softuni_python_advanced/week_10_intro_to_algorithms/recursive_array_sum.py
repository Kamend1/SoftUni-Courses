def calc_sum(n, idx):
    if idx == len(n) - 1:
        return n[idx]

    return n[idx] + calc_sum(n, idx + 1)

n = [int(x) for x in input().split()]
print(calc_sum(n, 0))
