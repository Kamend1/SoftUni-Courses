def rectangle(length: int, width: int) -> str:
    if type(length) != int  or type(width) != int:
        return "Enter valid values!"


    def area():
        rect_area = length * width
        return rect_area


    def perimeter():
        rect_perimeter = 2 * length + 2 * width
        return rect_perimeter

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))
