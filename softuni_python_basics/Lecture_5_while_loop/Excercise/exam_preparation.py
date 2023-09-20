number_fail_grades = int(input())
count_fails = 0
total_score = 0
number_problems = 0

while count_fails < number_fail_grades:
    problem_name = input()
    if problem_name == "Enough":
        average_score = total_score / number_problems
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {number_problems}")
        print(f"Last problem: {previous_problem_name}")
        break
    problem_score = int(input())
    if problem_score <= 4:
        previous_problem_name = problem_name
        count_fails += 1
        number_problems += 1
        total_score += problem_score
    else:
        previous_problem_name = problem_name
        number_problems += 1
        total_score += problem_score
else:
    print(f"You need a break, {number_fail_grades} poor grades.")
