student_courses = {}
data = []

user_command = input()

while True:
    if ":" not in user_command:
        course_searched = user_command
        break
    data.append(user_command)
    user_command = input()

for command in data:
    name, id_num, course = command.split(":")
    if id_num not in student_courses:
        student_courses[id_num] = {}

    student_courses[id_num]['name'] = name
    student_courses[id_num]['course'] = course

if "_" in course_searched:
    index = course_searched.index("_")
    course_searched = course_searched[0:index]+" "+course_searched[index +1:]

for id_num in student_courses.keys():
    if course_searched in student_courses[id_num]['course']:
        print(f"{student_courses[id_num]['name']} - {id_num}")
