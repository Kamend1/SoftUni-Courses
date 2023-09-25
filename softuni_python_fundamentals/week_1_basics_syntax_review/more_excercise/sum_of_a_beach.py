string = input()
counter = 0



for idx in range(len(string)):
    if (ord(string[idx]) == 87 or ord(string[idx]) == 119) and idx + 4 <= len(string):
        if (ord(string[idx + 1]) == 65 or ord(string[idx + 1]) == 97) and idx + 1 <= len(string):
            if (ord(string[idx + 2]) == 84 or ord(string[idx + 2]) == 116) and idx + 2 <= len(string):
                if (ord(string[idx + 3]) == 69 or ord(string[idx + 3]) == 101) and idx + 3 <= len(string):
                    if (ord(string[idx + 4]) == 82 or ord(string[idx + 4]) == 114) and idx + 4 <= len(string):
                        counter += 1
    if (ord(string[idx]) == 83 or ord(string[idx]) == 115) and idx + 2 <= len(string):
        if (ord(string[idx + 1]) == 65 or ord(string[idx + 1]) == 97) and idx + 1 <= len(string):
            if (ord(string[idx + 2]) == 78 or ord(string[idx + 2]) == 110) and idx + 2 <= len(string):
                if (ord(string[idx + 3]) == 68 or ord(string[idx + 3]) == 100) and idx + 3 <= len(string):
                    counter += 1
    if (ord(string[idx]) == 70 or ord(string[idx]) == 102) and idx + 3 <= len(string):
        if (ord(string[idx + 1]) == 73 or ord(string[idx + 1]) == 105) and idx + 1 <= len(string):
            if (ord(string[idx + 2]) == 83 or ord(string[idx + 2]) == 115) and idx + 2 <= len(string):
                if (ord(string[idx + 3]) == 72 or ord(string[idx + 3]) == 104) and idx + 3 <= len(string):
                    counter += 1
    if (ord(string[idx]) == 83 or ord(string[idx]) == 115) and idx + 2 <= len(string):
        if (ord(string[idx + 1]) == 85 or ord(string[idx + 1]) == 117) and idx + 1 <= len(string):
            if (ord(string[idx + 2]) == 78 or ord(string[idx + 2]) == 110) and idx + 2 <= len(string):
                counter += 1

print(counter)
