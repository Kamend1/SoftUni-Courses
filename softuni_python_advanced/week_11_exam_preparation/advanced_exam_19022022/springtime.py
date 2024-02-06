def start_spring(**kwargs):
    result = ""
    types_list_object = {}
    for object, type in kwargs.items():
        if type not in types_list_object:
            types_list_object[type] = []
        types_list_object[type].append(object)

    sorted_objects = dict(sorted(types_list_object.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, v in sorted_objects.items():
        result += f"{k}:\n"
        for element in sorted(v):
            result += f"-{element}\n"

    return(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
