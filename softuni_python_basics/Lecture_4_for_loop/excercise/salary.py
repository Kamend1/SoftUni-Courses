number_tabs = int(input())
salary = int(input())
penalty = 0

for i in range(number_tabs):
    name_tab = input()
    if name_tab == "Facebook":
        penalty += 150
        if penalty >= salary:
            print(f"You have lost your salary.")
            break
    elif name_tab == "Instagram":
        penalty += 100
        if penalty >= salary:
            print(f"You have lost your salary.")
            break
    elif name_tab == "Reddit":
        penalty += 50
        if penalty >= salary:
            print(f"You have lost your salary.")
            break

if penalty < salary:
    print(f"{salary - penalty:.0f}")
