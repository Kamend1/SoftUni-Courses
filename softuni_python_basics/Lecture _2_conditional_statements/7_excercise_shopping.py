budget_peter = float(input())
qty_videocards = int(input())
qty_cpus = int(input())
qty_ram = int(input())

price_videocards = 250
price_cpu = (qty_videocards * price_videocards) * 0.35
price_ram = (qty_videocards * price_videocards) * 0.1

amount_needed = (qty_videocards * price_videocards)\
                + (qty_cpus * price_cpu)\
                + (qty_ram * price_ram)
if qty_videocards > qty_cpus:
    amount_needed *= 0.85

difference = abs(budget_peter - amount_needed)

if budget_peter >= amount_needed:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
