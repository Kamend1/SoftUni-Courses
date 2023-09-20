point_first_x = float(input())
point_first_y = float(input())
point_second_x = float(input())
point_second_y = float(input())
point_test_x = float(input())
point_test_y = float(input())

if (point_test_x == point_first_x or point_test_x == point_second_x) \
        and (point_first_y <= point_test_y <= point_second_y):
    print("Border")
elif (point_test_y == point_first_y or point_test_y == point_second_y) \
        and (point_first_x <= point_test_x <= point_second_x):
    print("Border")
else:
    print("Inside / Outside")

