mine_output_list = []
mine_output_dict = {}

while True:
    user_command = input()
    if user_command == "stop":
        break
    mine_output_list.append(user_command)

for idx in range(len(mine_output_list)):
    if idx % 2 == 0:
        if mine_output_list[idx] not in mine_output_dict:
            mine_output_dict[mine_output_list[idx]] = int(mine_output_list[idx + 1])
        else:
            mine_output_dict[mine_output_list[idx]] += int(mine_output_list[idx + 1])

for item, qty in mine_output_dict.items():
    print(f"{item} -> {qty}")
