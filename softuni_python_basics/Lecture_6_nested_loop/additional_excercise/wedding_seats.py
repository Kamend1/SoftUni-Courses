last_sector_letter = input()
number_rows_first_sector = int(input())
number_seats_uneven_row = int(input())
seat_counter = 0

for sector in range(ord("A"), ord(last_sector_letter) + 1):
    for row in range(1, number_rows_first_sector + 1):
        if row % 2 != 0:
            for seat in range(97, 97 + number_seats_uneven_row):
                print(chr(sector) + str(row) + chr(seat))
                seat_counter += 1
        elif row % 2 == 0:
            for seat in range(97, 97 + number_seats_uneven_row + 2):
                print(chr(sector) + str(row) + chr(seat))
                seat_counter += 1
    number_rows_first_sector += 1

print(seat_counter)
