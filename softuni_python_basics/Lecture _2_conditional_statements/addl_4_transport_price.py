number_kilometers = int(input())
day_or_night = str(input())
starting_fee_taxi = 0.70
day_tariff_taxi = 0.79
night_tariff_taxi = 0.90
tariff_bus = 0.09
tariff_train = 0.06
amount_taxi_day = starting_fee_taxi + (number_kilometers * day_tariff_taxi)
amount_taxi_night = starting_fee_taxi + (number_kilometers * night_tariff_taxi)
amount_bus = number_kilometers * tariff_bus
amount_train = number_kilometers * tariff_train

if day_or_night == 'day':
    if number_kilometers < 20:
        print(f"{amount_taxi_day:.2f}")
    elif number_kilometers >= 100:
        print(f"{amount_train:.2f}")
    else:
        print(f"{amount_bus:.2f}")
else:
    if number_kilometers < 20:
        print(f"{amount_taxi_night:.2f}")
    elif number_kilometers >= 100:
        print(f"{amount_train:.2f}")
    else:
        print(f"{amount_bus:.2f}")
