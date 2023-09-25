start_ascii_index = int(input())
end_ascii_index = int(input())

while start_ascii_index <= end_ascii_index - 1:
    print(chr(start_ascii_index), end = " ")
    start_ascii_index += 1
print(chr(end_ascii_index))
