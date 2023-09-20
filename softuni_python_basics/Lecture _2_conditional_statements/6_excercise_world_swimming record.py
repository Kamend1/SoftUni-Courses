world_record_seconds = float(input())
distance_meters = float(input())
speed_meter_second = float(input())
number_slowdowns = (distance_meters // 15)
time_ivan = (distance_meters * speed_meter_second) + (number_slowdowns * 12.5)

if time_ivan < world_record_seconds:
    print(f'Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.')
else:
    time_exceed = time_ivan - world_record_seconds
    print(f'No, he failed! He was {time_exceed:.2f} seconds slower.')
