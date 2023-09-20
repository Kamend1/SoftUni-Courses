width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
volume = width_free_space * length_free_space * height_free_space
total_volume_used = 0
difference = volume - total_volume_used

while difference > 0:
    number_boxes_moved = input()
    if number_boxes_moved == "Done":
        difference = volume - total_volume_used
        print(f"{difference} Cubic meters left.")
        break
    else:
        if difference < int(number_boxes_moved):
            shortage = int(number_boxes_moved) - difference
            print(f"No more free space! You need {shortage} Cubic meters more.")
            break
        else:
            total_volume_used += int(number_boxes_moved)
            difference = volume - total_volume_used
