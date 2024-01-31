from collections import deque

food_supplies = [int(x) for x in input().split(", ")]
daily_stamina = deque(int(x) for x in input().split(", "))

peaks_queue = deque([
    (80, 'Vihren'),
    (90, 'Kutelo'),
    (100, 'Banski Suhodol'),
    (60, 'Polezhan'),
    (70, 'Kamenitza')
])

peak_climbed = []

while True:
    current_food = food_supplies.pop()
    current_stamina = daily_stamina.popleft()
    result = current_food + current_stamina
    current_peak = peaks_queue.popleft()
    value, peak_name = current_peak
    if result >= value:
        peak_climbed.append(peak_name)
    else:
        peaks_queue.appendleft(current_peak)

    if not peaks_queue:
        break

    if not daily_stamina:
        break

    if not food_supplies:
        break

if not peaks_queue:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if peak_climbed:
    result = "Conquered peaks:\n" + '\n'.join(peak_climbed)
    print(result)
