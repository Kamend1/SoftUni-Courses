def insertion_sort(nums):
    for i in range(1, len(nums)): # start from 1 because at 0 is the sorted part
        key = nums[i] # we take key because at shifting it will get lost
        j = i - 1 # we take the last value of the sorted part

        while j >= 0 and nums[j] > key: #until we reach the beginning and a postion to plase the key
            nums[j + 1] = nums[j] # we shift the element
            j -= 1 # we move left

        nums[j + 1] = key

    return nums

nums = [int(x) for x in input().split()]
insertion_sort(nums)
print(*nums)