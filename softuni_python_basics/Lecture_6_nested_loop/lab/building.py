number_floors = int(input())
number_rooms_per_floor = int(input())
print_string = ""

for apartment in range(number_rooms_per_floor):
    apartment = "L" + str(number_floors) + str(apartment)
    print_string += apartment + " "
print(print_string)
print_string = ""
for floor in range(number_floors -1, 0, -1):
    if floor % 2 == 0:
        for apartment in range(number_rooms_per_floor):
            apartment = "O" + str(floor) + str(apartment)
            print_string += apartment + " "
        print(print_string)
        print_string = ""
    elif floor % 2 != 0:
        for apartment in range(number_rooms_per_floor):
            apartment = "A" + str(floor) + str(apartment)
            print_string += apartment + " "
        print(print_string)
        print_string = ""
