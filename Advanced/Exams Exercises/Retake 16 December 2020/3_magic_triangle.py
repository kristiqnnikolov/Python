# Create a function called get_magic_triangle which will receive a single parameter (integer n) and
# it should create a magic triangle which follows those rules:
# •	We start with this simple triangle [[1], [1, 1]]
# •	We generate the next rows until we reach n amount of rows
# •	Each number in each row is equal to the sum of the two numbers right above it in the triangle
# •	If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
# Note: Submit only the function in the judge system
# Input
# •	There will be no inputs
# •	The function will be tested by passing different values of n
# •	You can test your function with the test code below
def get_magic_triangle(num_rows):
    result = []
    for n in range(num_rows):
        result.append([])
        result[n].append(1)
        for x in range(1, n):
            result[n].append(result[n - 1][x - 1] + result[n - 1][x])
        if n != 0:
            result[n].append(1)
    return result


get_magic_triangle(5)
