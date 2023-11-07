list_usernames = input().split(", ")

for name in list_usernames:
    username_is_valid = True
    for chr in name:
        if chr.isalnum() or chr == '_' or chr == '-':
            pass
        else:
            username_is_valid = False
    if len(name) < 3 or len(name) > 16:
        username_is_valid = False
    if username_is_valid:
        print(name)
