number_snowballs = int(input())
highest_score = 0
weight_high = 0
time_high = 0
quality_high = 0

for i in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    score = (weight / time) ** quality
    if score > highest_score:
        highest_score = score
        weight_high = weight
        time_high = time
        quality_high = quality

print(f"{weight_high} : {time_high} = {int(highest_score)} ({quality_high})")
