cake_width = int(input())
cake_length = int(input())
number_pieces = cake_width * cake_length
pieces_taken = 0

while number_pieces > 0:
    number_guests = input()
    if number_guests == "STOP":
        difference = number_pieces - pieces_taken
        print(f"{difference} pieces are left.")
        break
    if int(number_guests) <= number_pieces - pieces_taken:
        pieces_taken += int(number_guests)
    else:
        difference = int(number_guests) - (number_pieces - pieces_taken)
        print(f"No more cake left! You need {difference} pieces more.")
        break
