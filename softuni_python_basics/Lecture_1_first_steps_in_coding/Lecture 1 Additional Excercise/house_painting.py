x_height_house = float(input())
y_length_house = float(input())
h_height_roof = float(input())

roof_area_triangle = (x_height_house * h_height_roof) / 2
roof_area_side = x_height_house * y_length_house
roof_area = 2 * roof_area_side + 2 * roof_area_triangle

house_front_back = (2 * x_height_house * x_height_house) - (2 * 1.2)
house_side = (2 * y_length_house * x_height_house) - (1.5 * 1.5 * 2)
house_area = house_side + house_front_back

paint_roof_red = roof_area / 4.3
paint_house_green = house_area / 3.4

print(f"{paint_house_green:.2f}")
print(f"{paint_roof_red:.2f}")
