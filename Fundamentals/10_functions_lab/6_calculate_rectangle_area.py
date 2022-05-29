# Create a function that calculates and returns the area of a rectangle by given width and height.
# Print the result on the console.

def area(one_side, other_side):
    return one_side * other_side


one_side = int(input())
other_side = int(input())

result = area(one_side, other_side)
print(result)
