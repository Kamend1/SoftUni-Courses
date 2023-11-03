exam_results = {}

user_command = input()

while user_command != "exam finished":

    user_command = user_command.split("-")

    if user_command[1] != "banned":
        name = user_command[0]
        language = user_command[1]
        score = int(user_command[2])
        if language not in exam_results.keys():
            exam_results[language] = {}
        if name not in exam_results[language]:
            exam_results[language][name] = []
        exam_results[language][name].append(score)
    else:
        name = user_command[0]
        banned = user_command[1]
        for key, value in exam_results.items():
            if name in value:
                for idx in range(len(exam_results[key][name])):
                    exam_results[key][name][idx] = "banned"
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
