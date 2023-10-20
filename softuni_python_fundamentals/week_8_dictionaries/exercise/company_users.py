company_register = {}

user_command = input().split(" -> ")

while user_command[0] != "End":
    company = user_command[0]
    id_num = user_command[1]
    if company not in company_register:
        company_register[company] = []
    if id_num not in company_register[company]:
        company_register[company].append(id_num)

    user_command = input().split(" -> ")

for company, id_nums in company_register.items():
    print(f"{company}")
    for id_num in id_nums:
        print(f"-- {id_num}")
