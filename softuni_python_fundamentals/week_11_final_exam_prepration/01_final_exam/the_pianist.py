def add_piece(piece, composer, key, dictionary):
    result = ""
    if piece not in dictionary:
        dictionary[piece] = {}
        dictionary[piece]['composer'] = composer
        dictionary[piece]['key'] = key
        result = f"{piece} by {composer} in {key} added to the collection!"
    else:
        result = f"{piece} is already in the collection!"

    return result

def remove_piece(piece, dictionary: dict):
    result = ""
    if piece not in dictionary:
        result = f"Invalid operation! {piece} does not exist in the collection."
    else:
        dictionary.pop(piece)
        result = f"Successfully removed {piece}!"
    return result


def change_key(piece, new_key_value, dictionary):
    result = ""
    if piece not in dictionary:
        result = f"Invalid operation! {piece} does not exist in the collection."
    else:
        dictionary[piece]['key'] = new_key_value
        result = f"Changed the key of {piece} to {new_key_value}!"
    return result

collection = {}
initial_number_pieces = int(input())

for _ in range(initial_number_pieces):
    new_piece, current_composer, current_key = input().split("|")
    collection[new_piece] = {'composer': current_composer, 'key': current_key}

while True:
    user_command = input().split("|")
    if user_command[0] == "Stop":
        break
    elif user_command[0] == "Add":
        new_piece, current_composer, current_key = user_command[1], user_command[2], user_command[3]
        print(add_piece(new_piece, current_composer, current_key, collection))
    elif user_command[0] == "Remove":
        new_piece = user_command[1]
        print(remove_piece(new_piece, collection))
    elif user_command[0] == "ChangeKey":
        new_piece, new_key = user_command[1], user_command[2]
        print(change_key(new_piece, new_key, collection))

for piece, values in collection.items():
    print(f"{piece} -> Composer: {values['composer']}, Key: {values['key']}")
