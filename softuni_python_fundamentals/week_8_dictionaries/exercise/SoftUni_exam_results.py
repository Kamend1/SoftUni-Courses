exam_results = {}

user_command = input()

while user_command != "exam finished":

    user_command = user_command.split("-")

    if user_command[1] != "banned":
        if user_command[1] not in exam_results.keys():
            exam_results[user_command[1]] = {}
        if user_command[0] not in exam_results[user_command[1]]:
            exam_results[user_command[1]][user_command[0]] = []
        exam_results[user_command[1]][user_command[0]].append(user_command[2])
    else:
        for key, value in exam_results.items():
            if user_command[0] in value:
                exam_results[key][user_command[0]].pop()
                exam_results[key][user_command[0]].append("banned")
    user_command = input()

print("Results:")
for language, names in exam_results.items():
    for name, score in names.items():
      if score[0] != "banned":
        print(f"{name} | {max(score)}")

print("Submissions:")
for language, names in exam_results.items():
    submissions = 0
    for name, score in names.items():
        submissions += len(score)
    print(f"{language} - {submissions}")
