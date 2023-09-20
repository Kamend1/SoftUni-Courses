length = int(input())
width = int(input())
height = int(input())
percent_occuped_volume = float(input())

volume = length * width * height
volume_ltrs = volume / 1000
free_volume_ltrs = volume_ltrs - volume_ltrs * percent_occuped_volume/100

print(free_volume_ltrs)
