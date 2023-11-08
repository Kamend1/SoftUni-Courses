number_of_lines = int(input())

for line in range(number_of_lines):
    name = ""
    age = ""
    text = input()
    start_index_name = 0
    end_index_name = 0
    start_index_age = 0
    end_index_age = 0
    for idx in range(len(text)):
        if text[idx] == "@":
            start_index_name = idx
        if text[idx] == "|":
            end_index_name = idx
        if text[idx] == "#":
            start_index_age = idx
        if text[idx] == "*":
            end_index_age = idx
    name = text[start_index_name + 1:end_index_name]
    age = text[start_index_age + 1:end_index_age]
    print(f"{name} is {age} years old.")
