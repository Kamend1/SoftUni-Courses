def array_sum(numbers, idx):
    if idx == len(numbers) -1:
        return numbers[idx]
    return numbers[idx] + array_sum(numbers, idx + 1)

numbers = [int(x) for x in input().split()]
print(array_sum(numbers, 0))
