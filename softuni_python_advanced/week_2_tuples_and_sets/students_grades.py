count = int(input())
students = {}

for _ in range(count):
    name, grade = tuple(x for x in input().split())
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    print(f"{name} -> {' '.join(str('{:.2f}'.format(grade)) for grade in grades)} (avg: {sum(grades)/len(grades):.2f})")
