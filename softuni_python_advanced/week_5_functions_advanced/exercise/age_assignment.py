def age_assignment(*args, **kwargs):
    name_age_dict = {}
    for name in args:
        name_age_dict[name] = 0
        key = name[0]
        age = kwargs.get(key)
        name_age_dict[name] += age

    sorted_dict = sorted(name_age_dict.items(), key=lambda x: x[0])
    result = ''
    for person in sorted_dict:
        result += f"{person[0]} is {person[1]} years old.\n"
    return result

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))