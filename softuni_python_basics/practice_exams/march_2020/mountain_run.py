from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_per_meter_seconds = float(input())
slowdown = floor(distance_meters / 50) * 30

time_run = distance_meters * time_per_meter_seconds + slowdown
seconds_over = time_run - record_seconds

if record_seconds > time_run:
    print(f"Yes! The new record is {time_run:.2f} seconds.")
else:
    print(f"No! He was {seconds_over:.2f} seconds slower.")
