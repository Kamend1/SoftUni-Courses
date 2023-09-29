integer_list = [int(x) for x in input().split(" ")]
n = int(input())

sorted_list = sorted(integer_list)
small_list = sorted_list[0:n]

for element in small_list:
    integer_list.remove(element)

for i in range(len(integer_list) - 1):
    print(integer_list[i], end=", ")
print(integer_list[len(integer_list) - 1])
