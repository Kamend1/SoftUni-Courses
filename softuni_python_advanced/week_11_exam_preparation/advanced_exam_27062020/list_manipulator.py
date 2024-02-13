def list_manipulator(num_list, *args):
    if args[0] == 'remove':
        if args[1] == 'beginning':
            num_list = num_list[::-1]
            if len(args) > 2:
                for idx in range(args[2]):
                    num_list.pop()
            else:
                num_list.pop()
            num_list = num_list[::-1]
        elif args[1] == 'end':
            if len(args) > 2:
                for idx in range(args[2]):
                    num_list.pop()
            else:
                num_list.pop()
    elif args[0] == 'add':
        if args[1] == 'beginning':
            for idx in range(2, len(args)):
                num_list.insert(idx - 2, args[idx])
        elif args[1] == 'end':
            for idx in range(2, len(args)):
                num_list.append(args[idx])

    return num_list

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
