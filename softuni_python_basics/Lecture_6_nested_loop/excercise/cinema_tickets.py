user_command = input()
total_tickets = 0
movie_attendance = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while user_command != "Finish":
    number_seats = int(input())
    for seat in range(number_seats):
        type_ticket = input()
        if type_ticket == "student":
            student_tickets += 1
            total_tickets += 1
            movie_attendance += 1
        elif type_ticket == "standard":
            standard_tickets += 1
            total_tickets += 1
            movie_attendance += 1
        elif type_ticket == "kid":
            kid_tickets += 1
            total_tickets += 1
            movie_attendance += 1
        elif type_ticket == "End":
            break
    percent_hall_full = movie_attendance * 100 / number_seats
    print(f"{user_command} - {percent_hall_full:.2f}% full.")
    movie_attendance = 0
    user_command = input()

percent_student_tickets = student_tickets * 100 / total_tickets
percent_standard_tickets = standard_tickets * 100 / total_tickets
percent_kid_tickets = kid_tickets * 100 / total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")
