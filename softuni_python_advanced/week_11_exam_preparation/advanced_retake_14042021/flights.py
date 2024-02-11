from collections import deque

def flights(*args):
    passenger_count_dict = {}
    flight_info_queue = deque(arg for arg in args)
    while flight_info_queue:
        current_flight = flight_info_queue.popleft()
        if current_flight == 'Finish':
            break
        else:
            current_number = flight_info_queue.popleft()
            passenger_count_dict[current_flight] = passenger_count_dict.get(current_flight, 0) + current_number

    return passenger_count_dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

