from functools import reduce


def operate(operator: str, *nums):
    result = 0
    if operator == '+':
        result = reduce(lambda a, b: a + b, nums)
    elif operator == '-':
        result = reduce(lambda a, b: a - b, nums)
    elif operator == '*':
        result = reduce(lambda a, b: a * b, nums)
    elif operator == ('/'):
        result = reduce(lambda a, b: a / b, nums)
    return result

print(operate("/", 3, 0, 3))
