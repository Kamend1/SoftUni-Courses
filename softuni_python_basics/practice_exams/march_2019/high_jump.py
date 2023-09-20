desired_height = int(input())
jumps_counter = 0
failed_jumps_counter = 0
current_practice_height = 0
practice_is_not_over = True
reached_desired_height = False
current_practice_height = desired_height - 30

while practice_is_not_over:
    current_attempt = int(input())
    if current_attempt > current_practice_height:
        jumps_counter += 1
        current_practice_height += 5
        failed_jumps_counter = 0
        if current_practice_height > desired_height:
            reached_desired_height = True
            break
    else:
        jumps_counter += 1
        failed_jumps_counter += 1

    if failed_jumps_counter == 3:
        practice_is_not_over = False
        break


if not practice_is_not_over:
    print(f"Tihomir failed at {current_practice_height}cm after {jumps_counter} jumps.")
if reached_desired_height:
    print(f"Tihomir succeeded, he jumped over {desired_height}cm after {jumps_counter} jumps.")
