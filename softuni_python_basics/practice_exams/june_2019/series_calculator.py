from math import floor
name_serial = str(input())
number_seasons = int(input())
number_epizodes = int(input())
clean_time_epizode = float(input())
commercials = clean_time_epizode * 0.20 * number_epizodes * number_seasons
additional_time = number_seasons * 10
total_time = floor(number_epizodes * clean_time_epizode * number_seasons + commercials + additional_time)

print(f"Total time needed to watch the {name_serial} series is {total_time} minutes.")
