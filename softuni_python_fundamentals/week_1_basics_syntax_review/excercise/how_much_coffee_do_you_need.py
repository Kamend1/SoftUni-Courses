user_event_input = input()
coffee_count = 0

while user_event_input != "END":
    if user_event_input == "cat" or user_event_input == "dog" \
            or user_event_input == "coding" or user_event_input == "movie":
        coffee_count += 1
    elif user_event_input == "CAT" or user_event_input == "DOG" \
            or user_event_input == "CODING" or user_event_input == "MOVIE":
        coffee_count += 2
    else:
        coffee_count += 0

    user_event_input = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
