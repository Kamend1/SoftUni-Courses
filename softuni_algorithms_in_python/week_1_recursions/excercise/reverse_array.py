def reverse_array(arr):
    if not arr:
        return
    print(arr[-1], end=' ')
    reverse_array(arr[:-1])

# Example usage
input_array = input().split()
reverse_array(input_array)
