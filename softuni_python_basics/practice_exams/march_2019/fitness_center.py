number_visitors = int(input())
number_work_out = 0
number_protein = 0
number_back = 0
number_chest = 0
number_legs = 0
number_abs = 0
number_shake = 0
number_bar = 0

for i in range(number_visitors):
    purpose_visit = input()
    if purpose_visit == "Back" or purpose_visit == "Chest" or purpose_visit == "Legs" \
            or purpose_visit == "Abs":
        number_work_out += 1
        if purpose_visit == "Back":
            number_back += 1
        elif purpose_visit == "Chest":
            number_chest += 1
        elif purpose_visit == "Legs":
            number_legs += 1
        elif purpose_visit == "Abs":
            number_abs += 1
    elif purpose_visit == "Protein shake" or purpose_visit == "Protein bar":
        number_protein += 1
        if purpose_visit == "Protein shake":
            number_shake += 1
        elif purpose_visit == "Protein bar":
            number_bar += 1

percent_work_out = number_work_out * 100 / number_visitors
percent_protein = number_protein * 100 / number_visitors

print(f"{number_back} - back")
print(f"{number_chest} - chest")
print(f"{number_legs} - legs")
print(f"{number_abs} - abs")
print(f"{number_shake} - protein shake")
print(f"{number_bar} - protein bar")
print(f"{percent_work_out:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")
