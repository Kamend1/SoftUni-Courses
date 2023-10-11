text = input()

sorted_list = [char for char in text if char not in ['a', 'o', 'u', 'e', 'i']]

new_text = "".join(sorted_list)
print(new_text)
