n = int(input())
there_is_no_odd = True

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        continue
    else:
        print(f"{number} is odd!")
        there_is_no_odd = False
        break

if there_is_no_odd:
    print("All numbers are even.")
