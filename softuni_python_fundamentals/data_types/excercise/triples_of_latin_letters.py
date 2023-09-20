n = int(input())
first_chr = 97
second_chr = 97
third_chr = 97

for i in range(n):
    for k in range(n):
        for j in range(n):
            print(f"{chr(first_chr + i)}{chr(second_chr + k)}{chr(third_chr + j)}")
