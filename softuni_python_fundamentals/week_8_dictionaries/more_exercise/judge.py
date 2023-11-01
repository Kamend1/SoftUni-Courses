scores_by_contest = {}
scores_by_user = {}
users_total_score = {}
contest_participants = {}

while True:
    user_command = input()
    if user_command == "no more time":
        break
    user, contest, score = user_command.split(" -> ")

    if contest not in scores_by_contest:
        scores_by_contest[contest] = {}
    if user not in scores_by_contest[contest]:
        scores_by_contest[contest][user] = int(score)
    else:
        if scores_by_contest[contest][user] < int(score):
            scores_by_contest[contest][user] = int(score)

    if user not in scores_by_user:
        scores_by_user[user] = {}
    if contest not in scores_by_user[user]:
        scores_by_user[user][contest] = int(score)
    else:
        if scores_by_user[user][contest] < int(score):
            scores_by_user[user][contest] = int(score)

for contest, scores in scores_by_contest.items():
    for name, score in scores.items():
        if name not in users_total_score:
            users_total_score[name] = score
        else:
            users_total_score[name] += score

for contest, participants in scores_by_contest.items():
    if contest not in contest_participants:
        contest_participants[contest] = 0
    for participant in participants.keys():
        contest_participants[contest] += 1


for contest, scores in scores_by_contest.items():
    print(f"{contest}: {contest_participants[contest]} participants")
    student_counter = 0
    for name, score in sorted(scores.items(), key=lambda x: (-x[1], x[0])):
        student_counter += 1
        print(f"{student_counter}. {name} <::> {score}")

print("Individual standings:")
counter = 0
for student, total_score in sorted(users_total_score.items(), key=lambda x: (-x[1], x[0])):
    counter += 1
    print(f"{counter}. {student} -> {total_score}")
