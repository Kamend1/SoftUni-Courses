from collections import deque

initial_fuel_seq = [int(x) for x in input().split()]
additional_consumption = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

altitude_counter = 0

for _ in range(len(fuel_needed)):
    result = (initial_fuel_seq.pop() - additional_consumption.popleft()) - fuel_needed.popleft()
    if result >= 0:
        altitude_counter += 1
        print(f"John has reached: Altitude {altitude_counter}")
        if altitude_counter == 4:
            print("John has reached all the altitudes and managed to reach the top!")
    else:
        print(f"John did not reach: Altitude {altitude_counter + 1}")
        if altitude_counter > 0:
            altitudes = [f"Altitude {i}" for i in range(1, altitude_counter + 1)]
            print(f"John failed to reach the top.\n"
                  f"Reached altitudes: {', '.join(altitudes)}")
        else:
            print("John failed to reach the top.\nJohn didn't reach any altitude.")
        break
