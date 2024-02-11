from collections import deque

jobs = deque(int(x) for x in input().split(', '))
index = int(input())
int_task = jobs[index]
number_of_cycles = 0


for idx in range(len(jobs)):
    if jobs[idx] < int_task:
        number_of_cycles += jobs[idx]


    if jobs[idx] == int_task:
        if idx < index:
            number_of_cycles += jobs[idx]


print(number_of_cycles + int_task)
