nums = [int(x) for x in input().split()]

is_sorted = False
filled_counter = 0
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(nums) - filled_counter):
        if nums[idx] < nums[idx - 1]:
            nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
            is_sorted = False
    filled_counter += 1

print(*nums, sep=' ')
