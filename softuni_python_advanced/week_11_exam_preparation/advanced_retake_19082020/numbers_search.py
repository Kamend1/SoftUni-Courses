def numbers_searching(*nums):
    duplicate_numbers = set()
    missing_numbers = []
    nums = sorted(nums)
    for idx in range(len(nums) - 1):
        first_num = nums[idx]
        next_num = nums[idx + 1]
        if first_num == next_num:
            duplicate_numbers.add(nums[idx])
        if first_num != next_num and first_num + 1 < next_num:
            missing_numbers.append(first_num + 1)



    return [missing_numbers[0], [num for num in sorted(duplicate_numbers)]]

# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))