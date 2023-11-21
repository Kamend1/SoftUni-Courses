import re

racer_list = input().split(", ")
pattern_special_char = r"\W+"
pattern_numbers = r"[0-9]+"
pattern_letters = r"[a-zA-Z]+"
racer_scores_dict = {}

string = input()
while string != "end of race":
    distance = 0
    sorted_string = re.sub(pattern_special_char, "", string)
    letter_string = re.sub(pattern_numbers, "", sorted_string)
    number_string = re.sub(pattern_letters, "", sorted_string)
    for char in number_string:
        distance += int(char)
    if letter_string in racer_list:
        if letter_string not in racer_scores_dict:
            racer_scores_dict[letter_string] = 0
        racer_scores_dict[letter_string] += distance
    string = input()

racer_scores_dict = dict(sorted(racer_scores_dict.items(), key=lambda x: x[1], reverse=True))
winners_list = []
for key in racer_scores_dict.keys():
    winners_list.append(key)

winners = f"""
1st place: {winners_list[0]}
2nd place: {winners_list[1]}
3rd place: {winners_list[2]}
"""
print(winners)
