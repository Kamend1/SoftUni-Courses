import sys
from math import ceil
number_baked = int(input())
packets_sugar = 0
packets_flour = 0
weight_packet_sugar_grams = 950
weight_packet_flour_grams = 750
total_sugar = 0
total_flour = 0
max_weight_flour = -sys.maxsize
max_weight_sugar = -sys.maxsize


for i in range(number_baked):
    current_qty_sugar_grams = int(input())
    current_qty_flour_grams = int(input())
    total_sugar += current_qty_sugar_grams
    total_flour += current_qty_flour_grams
    if current_qty_sugar_grams > max_weight_sugar:
        max_weight_sugar = current_qty_sugar_grams
    if current_qty_flour_grams > max_weight_flour:
        max_weight_flour = current_qty_flour_grams

packets_flour = ceil(total_flour / weight_packet_flour_grams)
packets_sugar = ceil(total_sugar / weight_packet_sugar_grams)

print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_weight_flour} grams, max used sugar is {max_weight_sugar} grams.")
