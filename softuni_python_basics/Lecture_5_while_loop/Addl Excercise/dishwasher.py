number_detergent_bottles = int(input())
wash_cycle_counter = 0
qty_detergent = number_detergent_bottles * 750
detergent_is_over = False
user_command_input = input()
detergent_per_plate = 5
detergent_per_pot = 15
plates_washed = 0
pots_washed = 0

while user_command_input != "End":
    wash_cycle_counter += 1
    if wash_cycle_counter % 3 == 0:
        current_objects_washed = int(user_command_input)
        current_qty_detergent = current_objects_washed * detergent_per_pot
        qty_detergent -= current_qty_detergent
        pots_washed += current_objects_washed
    else:
        current_objects_washed = int(user_command_input)
        current_qty_detergent = current_objects_washed * detergent_per_plate
        qty_detergent -= current_qty_detergent
        plates_washed += current_objects_washed
    if qty_detergent < 0:
        detergent_is_over = True
        break
    user_command_input = input()

if detergent_is_over:
    print(f"Not enough detergent, {abs(qty_detergent)} ml. more necessary!")
else:
    print('Detergent was enough!')
    print(f'{plates_washed} dishes and {pots_washed} pots were washed.')
    print(f'Leftover detergent {qty_detergent} ml.')
