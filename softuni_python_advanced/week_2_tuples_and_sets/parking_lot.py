counter = int(input())
parking_lot = set()

for _ in range(counter):
    command, plate = input().split(', ')
    if command == "IN":
        parking_lot.add(plate)
    elif command == "OUT":
        parking_lot.remove(plate)

if parking_lot:
    for plate in parking_lot:
        print(plate)
else:
    print('Parking Lot is Empty')
