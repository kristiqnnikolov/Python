# Create a function called rectangle(). It must have two parameters - length and width.
# First, you need to check if the given arguments are integers:
# •	If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
# Create two inner functions:
# •	area() - returns the area of the rectangle with the given length and width
# •	perimeter() - returns the perimeter of the rectangle with the given length and width
# In the end, the rectangle function should return a string containing the
# area and the perimeter of a rectangle in the following format:
# "Rectangle area: {ract_area}
# Rectangle perimeter: {rect_perim}"
def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return length + length + width + width

    if type(length) == int and type(width) == int:
        a = area()
        b = perimeter()
        return f"Rectangle area: {a}\nRectangle perimeter: {b}"
    else:
        return f"Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))
