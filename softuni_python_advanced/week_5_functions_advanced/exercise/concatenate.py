def concatenate(*args, **kwargs):
    string = ''.join(args)
    for k, v in kwargs.items():
        if k in string:
            string = string.replace(k, v, -1)
    return string

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))