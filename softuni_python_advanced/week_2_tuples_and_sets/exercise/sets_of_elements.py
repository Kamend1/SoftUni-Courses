n, m = input().split()
set_1 = set()
set_2 = set()

for _ in range(int(n)):
    num = input()
    set_1.add(num)
for _ in range(int(m)):
    num = input()
    set_2.add(num)

print(*set_1.intersection(set_2), sep='\n')
