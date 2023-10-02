def min_max_sum(numbers):
    result_min = min(numbers)
    result_max = max(numbers)
    result_sum = sum(numbers)
    print(f"The minimum number is {result_min}\nThe maximum number is {result_max}\nThe sum number is: {result_sum}")

numbers = [int(x) for x in input().split()]

min_max_sum(numbers)
