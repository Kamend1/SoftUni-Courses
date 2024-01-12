number_guests = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(number_guests):
    reservation = input()
    if reservation[0].isdigit():
        vip_guests.add(reservation)
    else:
        regular_guests.add(reservation)

visitor = input()
while visitor != 'END':
    if visitor[0].isdigit():
        vip_guests.remove(visitor)
    else:
        regular_guests.remove(visitor)
    visitor = input()

vip_guests = sorted(vip_guests)
regular_guests = sorted(regular_guests)

print(len(vip_guests) + len(regular_guests))
print(*vip_guests, *regular_guests, sep='\n')
