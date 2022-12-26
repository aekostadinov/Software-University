"""Create a function called rectangle(). It must have two parameters - length and width.
First, you need to check if the given arguments are integers:
    -If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
Create two inner functions:
    -area() - returns the area of the rectangle with the given length and width
    -perimeter()- returns the perimeter of the rectangle with the given length and width
In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle
in the following format:
"Rectangle area: {ract_area}
Rectangle perimeter: {rect_perim}"""

def rectangle(lenght, width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return "Enter valid values!"
    def area():
        react_area = lenght * width
        return f"Rectangle area: {react_area}"
    def perimeter():
        react_perim = 2 * (lenght + width)
        return f"Rectangle perimeter: {react_perim}"
    return area() + "\n" + perimeter()

print(rectangle(2, 10))

