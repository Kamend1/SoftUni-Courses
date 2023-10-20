def vertical_bar_op(side_name: str, user: str, dictionary: dict):
    if side_name not in dictionary:
        dictionary[side_name] = []
    user_in_dictionary = False
    for key in dictionary.keys():
        if user in dictionary[key]:
            user_in_dictionary = True
    if not user_in_dictionary:
        dictionary[side_name].append(user)

    return dictionary

def arrow_op(side_name, user_name_1, dictionary):
    for key, name in dictionary.items():
        if user_name_1 in name:
            dictionary[key].remove(user_name_1)

    if side_name not in dictionary.keys():
        dictionary[side_name] = []

    dictionary[side_name].append(user_name_1)
    print(f"{user_name_1} joins the {side_name} side!")
    return dictionary

user_command = input()
force_dictionary = {}

while user_command != "Lumpawaroo":
    if "|" in user_command:
        user_command = user_command.split("|")
        force_side = user_command[0].rstrip()
        user_name = user_command[1].lstrip()
        force_dictionary = vertical_bar_op(force_side, user_name, force_dictionary)
    elif "->" in user_command:
        user_command = user_command.split("->")
        force_side = user_command[1].lstrip()
        user_name = user_command[0].rstrip()
        force_dictionary = arrow_op(force_side, user_name, force_dictionary)
    user_command = input()

for side, member in force_dictionary.items():
    if len(member) > 0:
        print(f"Side: {side}, Members: {len(member)}")
        for user in member:
            print(f"! {user}")
