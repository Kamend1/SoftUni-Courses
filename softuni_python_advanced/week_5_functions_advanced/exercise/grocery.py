def grocery_store(**kwargs):
    string = ''
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for k, v in sorted_dict:
        string += f"{k}: {v}\n"
    return string

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
