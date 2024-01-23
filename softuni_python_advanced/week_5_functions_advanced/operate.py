def operate(operator: str, *nums):
    result = 0
    if operator == '+':
        result = 0
        for num in nums:
            result += num
    elif operator == '-':
        result = nums[0]
        for num in nums[1:]:
            result -= num
    elif operator == '*':
        result = nums[0]
        for num in nums[1:]:
            result *= num
    elif operator == ('/'):
        result = nums[0]
        for num in nums[1:]:
            if num != 0:
                result /= num
    return result

print(operate("/", 3, 0, 3))
