def enroll(dictionary, name):
    if name not in dictionary:
        dictionary[name] = []
    else:
        print(f"{name} is already enrolled.")
    return dictionary


def learn(dictionary, name, skill):
    if name in dictionary:
        if skill in dictionary[name]:
            print(f"{name} has already learnt {skill}.")
        else:
            dictionary[name].append(skill)
    else:
        print(f"{name} doesn't exist.")
    return dictionary


def unlearn(dictionary, name, skill):
    if name in dictionary:
        if skill not in dictionary[name]:
            print(f"{name} doesn't know {skill}.")
        else:
            dictionary[name].remove(skill)
    else:
        print(f"{name} doesn't exist.")
    return dictionary


hero_dict = {}

user_command = input()

while user_command != "End":
    actions = user_command.split()
    if actions[0] == "Enroll":
        hero_name = actions[1]
        hero_dict = enroll(hero_dict, hero_name)
    elif actions[0] == "Learn":
        hero_name = actions[1]
        spell = actions[2]
        hero_dict = learn(hero_dict, hero_name, spell)
    elif actions[0] == "Unlearn":
        hero_name = actions[1]
        spell = actions[2]
        hero_dict = unlearn(hero_dict, hero_name, spell)

    user_command = input()

print("Heroes:")
for name, skills in hero_dict.items():
    print("== " + name + ":", end=' ')
    print(", ".join(skills))
