#Град	0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
#Sofia	5%	7%	8%	12%
#Varna	4.5%	7.5%	10%	13%
#Plovdiv	5.5%	8%	12%	14.5%

city = str(input())
volume_sales = float(input())
amount_commission = 0

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        amount_commission = volume_sales * 0.05
    elif 500 < volume_sales <= 1000:
        amount_commission = volume_sales * 0.07
    elif 1000 < volume_sales <= 10000:
        amount_commission = volume_sales * 0.08
    elif volume_sales > 10000:
        amount_commission = volume_sales * 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= volume_sales <= 500:
        amount_commission = volume_sales * 0.045
    elif 500 < volume_sales <= 1000:
        amount_commission = volume_sales * 0.075
    elif 1000 < volume_sales <= 10000:
        amount_commission = volume_sales * 0.10
    elif volume_sales > 10000:
        amount_commission = volume_sales * 0.13
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        amount_commission = volume_sales * 0.055
    elif 500 < volume_sales <= 1000:
        amount_commission = volume_sales * 0.08
    elif 1000 < volume_sales <= 10000:
        amount_commission = volume_sales * 0.12
    elif volume_sales > 10000:
        amount_commission = volume_sales * 0.145
    else:
        print("error")
else:
    print("error")

if amount_commission != 0:
    print(f"{amount_commission:.2f}")
