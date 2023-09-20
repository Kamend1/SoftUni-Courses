number_bitcoin = int(input())
number_yuan = float(input())
commission = float(input())

bitcoin_bgn = 1168
yuan_usd  = 0.15
usd_bgn = 1.76
eur_bgn = 1.95

amount_bitcoin_eur = number_bitcoin * bitcoin_bgn / eur_bgn
amount_yuan = number_yuan * yuan_usd * usd_bgn / eur_bgn

total_amount = (amount_bitcoin_eur + amount_yuan) * (1 - commission / 100)
print(f"{total_amount:.2f}")
