version_number_list = input().split(".")
sum_version_number = ""
new_sum_version_number = ""

for digit in version_number_list:
    sum_version_number += digit
new_sum_version_number = str(int(sum_version_number) + 1)
version_number_list.clear()
for new_digit in new_sum_version_number:
    version_number_list.append(new_digit)
print(*version_number_list, sep=".")
