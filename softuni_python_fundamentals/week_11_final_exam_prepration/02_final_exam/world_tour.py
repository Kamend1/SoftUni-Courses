def add_stop(index, old_string, new_string):
    result = old_string
    if 0 <= index < len(old_string):
        result = old_string[:index] + new_string + old_string[index:]
    return result

def remove_stop(start_index, end_index, string):
    result = string
    if 0 <= start_index < len(string) and 0 <= end_index < len(string):
        result = string[:start_index] + string[end_index + 1:]
    return result


def switch_stop(pattern, substitute, string):
    result = string
    if pattern in string:
        result = string.replace(pattern, substitute)
    return result


travel_stops = input()

while True:
    user_command = input()
    if user_command == "Travel":
        break
    commands = user_command.split(":")
    if commands[0] == "Add Stop":
        travel_stops = add_stop(int(commands[1]), travel_stops, commands[2])
        print(travel_stops)
    elif commands[0] == "Remove Stop":
        travel_stops = remove_stop(int(commands[1]), int(commands[2]), travel_stops)
        print(travel_stops)
    elif commands[0] == "Switch":
        travel_stops = switch_stop(commands[1], commands[2], travel_stops)
        print(travel_stops)

print(f"Ready for world tour! Planned stops: {travel_stops}")
