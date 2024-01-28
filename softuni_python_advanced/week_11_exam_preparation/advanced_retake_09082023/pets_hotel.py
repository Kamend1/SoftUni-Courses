from collections import deque


def accommodate_new_pets(capacity, max_weight, *pets):
    accommodated_pets = {}
    heavy_pets = []
    pets = deque(pets)
    result = ""

    while pets:
        pet = pets.popleft()
        pet_type, pet_weight = pet

        if pet_weight <= max_weight:
            if pet_type not in accommodated_pets:
                accommodated_pets[pet_type] = 0
            accommodated_pets[pet_type] += 1
            capacity -= 1
        else:
            heavy_pets.append(pet)

        if capacity == 0:
            break


    if not pets:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        result += f"You did not manage to accommodate all pets!\n"

    accommodated_pets = dict(sorted(accommodated_pets.items(), key=lambda x: x[0]))
    result += f"Accommodated pets:\n"
    for k, v in accommodated_pets.items():
        result += (f"{k}: {v}\n")

    return result


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

