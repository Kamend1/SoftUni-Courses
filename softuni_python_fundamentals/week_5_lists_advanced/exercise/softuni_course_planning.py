courses = input().split(", ")
user_command = input()

while user_command != "course start":
    user_command_list = user_command.split(":")
    if user_command_list[0] == "Add":
        if user_command_list[1] not in courses:
            courses.append(user_command_list[1])
    elif user_command_list[0] == "Insert":
        if user_command_list[1] not in courses:
            courses.insert(int(user_command_list[2]), user_command_list[1])
    elif user_command_list[0] == "Remove":
        if user_command_list[1] in courses:
            courses.remove(user_command_list[1])
    elif user_command_list[0] == "Swap":
        if user_command_list[1] in courses and user_command_list[2] in courses:
            idx1 = courses.index(user_command_list[1])
            idx2 = courses.index(user_command_list[2])
            courses[idx1], courses[idx2] = courses[idx2], courses[idx1]
            exercise = user_command_list[2] + "-" + "Exercise"
            if exercise in courses:
                courses.remove(exercise)
                courses.insert(idx1 + 1, exercise)
    elif user_command_list[0] == "Exercise":
        new_course = user_command_list[1] + "-" + "Exercise"
        if user_command_list[1] in courses and new_course not in courses:
            idx = courses.index(user_command_list[1])
            courses.insert(idx + 1, new_course)
        elif user_command_list[1] not in courses:
            courses.append(user_command_list[1])
            courses.append(user_command_list[1] + "-" + "Exercise")

    user_command = input()

for index, course in enumerate(courses):
    print(f"{index + 1}.{course}", end="")
    print()
