country = input()
type_object = input()
difficulty_score = 0
execution_score = 0

if country == "Russia":
    if type_object == "ribbon":
        difficulty_score = 9.100
        execution_score = 9.400
    elif type_object == "hoop":
        difficulty_score = 9.300
        execution_score = 9.800
    elif type_object == "rope":
        difficulty_score = 9.600
        execution_score = 9.000
elif country == "Bulgaria":
    if type_object == "ribbon":
        difficulty_score = 9.600
        execution_score = 9.400
    elif type_object == "hoop":
        difficulty_score = 9.550
        execution_score = 9.750
    elif type_object == "rope":
        difficulty_score = 9.500
        execution_score = 9.400
elif country == "Italy":
    if type_object == "ribbon":
        difficulty_score = 9.200
        execution_score = 9.500
    elif type_object == "hoop":
        difficulty_score = 9.450
        execution_score = 9.350
    elif type_object == "rope":
        difficulty_score = 9.700
        execution_score = 9.150

total_score = difficulty_score + execution_score
total_score_deff_percent = (20 - total_score) * 100 / 20

print(f"The team of {country} get {total_score:.3f} on {type_object}.")
print(f"{total_score_deff_percent:.2f}%")
