def binary_search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2  # Calculate mid_idx within the loop
        if nums[mid_idx] == target:
            return mid_idx
        elif nums[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return -1

nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))
