courses = {}

user_command = input().split(" : ")

while user_command[0] != "end":
    course, name = user_command[0], user_command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
    user_command = input().split(" : ")

for key, course in courses.items():
    print(f"{key}: {len(course)}")
    for student in course:
        print(f"-- {student}")
