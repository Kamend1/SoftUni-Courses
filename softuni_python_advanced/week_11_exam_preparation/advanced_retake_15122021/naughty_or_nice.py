def naughty_or_nice_list(list_kids, * args, **kwargs):
    kids_sort = {'Nice': [], 'Naughty': [], 'not_found': []}

    for arg in args:
        number, type_kid = arg.split('-')

        temp_list = []

        for kid in list_kids:
            if kid[0] == int(number):
                temp_list.append(kid)

        if len(temp_list) == 1:
            kids_sort[type_kid].append(temp_list[0][1])
            list_kids.remove(temp_list[0])


    for name, category in kwargs.items():

        temp_list = []

        for kid in list_kids:
            if kid[1] == name:
                temp_list.append(kid)

        if len(temp_list) == 1:
            kids_sort[category].append(temp_list[0][1])
            list_kids.remove(temp_list[0])

    for kid in list_kids:
        kids_sort['not_found'].append(kid[1])

    result = ""
    if kids_sort['Nice']:
        result += f"Nice: {', '.join(kids_sort['Nice'])}\n"
    if kids_sort['Naughty']:
        result += f"Naughty: {', '.join(kids_sort['Naughty'])}\n"
    if kids_sort['not_found']:
        result += f"Not found: {', '.join(kids_sort['not_found'])}"

    if result:
        return result
    else:
        return None

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
        (4, "Katy")
    ],
    # "3-Nice",
    "1-Naughty",
    "1-Naughty",
    # Amy="Nice",
    Katy="Naughty",
))
