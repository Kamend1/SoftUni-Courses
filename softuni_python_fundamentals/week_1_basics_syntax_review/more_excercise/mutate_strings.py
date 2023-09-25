string_1, string_2 = input(), input()

string_1_list = []
string_2_list = []

for char in string_1:
    string_1_list.append(char)

for char in string_2:
    string_2_list.append(char)

for idx in range(len(string_1_list)):
    if string_1_list[idx] != string_2_list[idx]:
        string_1_list.pop(idx)
        string_1_list.insert(idx, string_2_list[idx])
        print("".join(string_1_list))
