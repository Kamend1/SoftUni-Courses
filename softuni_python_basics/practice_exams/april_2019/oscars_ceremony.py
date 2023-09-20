hall_rent = int(input())
statues = hall_rent * 0.70
catering = statues * 0.85
sound = catering / 2

amount_needed = hall_rent + statues + catering + sound

print(f"{amount_needed:.2f}")
