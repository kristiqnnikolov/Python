# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.

def perfect(n):
    total = 0
    if n > 1:
        for divider in range(1, n):
            if n % divider == 0:
                if n != divider:
                    total += divider

        return total


integer = int(input())
if perfect(integer) == integer:
    print(f"We have a perfect number!")
else:
    print(f"It's not so perfect.")
