contest_password = {}

while True:
    user_input = input()
    if user_input == "end of contests":
        break
    contest, password = user_input.split(":")
    contest_password[contest] = password

contest_results_key_contest = {}
contest_results_key_candidate = {}

while True:
    user_command = input()
    if user_command == "end of submissions":
        break
    contest_name, password_check, candidate, score = user_command.split("=>")
    if contest_name in contest_password.keys() and contest_password[contest_name] == password_check:
        if contest_name not in contest_results_key_contest:
            contest_results_key_contest[contest_name] = {}
        if candidate not in contest_results_key_contest[contest_name]:
            contest_results_key_contest[contest_name][candidate] = int(score)
        else:
            if contest_results_key_contest[contest_name][candidate] < int(score):
                contest_results_key_contest[contest_name][candidate] = int(score)
    if contest_name in contest_password.keys() and contest_password[contest_name] == password_check:
        if candidate not in contest_results_key_candidate:
            contest_results_key_candidate[candidate] = {}
        if contest_name not in contest_results_key_candidate[candidate]:
            contest_results_key_candidate[candidate][contest_name] = int(score)
        else:
            if contest_results_key_candidate[candidate][contest_name] < int(score):
                contest_results_key_candidate[candidate][contest_name] = int(score)

student_total_score = {}
max_total_score = 0
max_name = ""

for contest_name, results in contest_results_key_contest.items():
    for name, score in results.items():
        if name not in student_total_score:
            student_total_score[name] = score
        else:
            student_total_score[name] += score

for name, total_score in student_total_score.items():
    if total_score > max_total_score:
        max_total_score = total_score
        max_name = name

print(f"Best candidate is {max_name} with total {max_total_score} points.")
print("Ranking:")
for name, contest_results in sorted(contest_results_key_candidate.items()):
    print(name)
    for contest, score in sorted(contest_results.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {score}")
