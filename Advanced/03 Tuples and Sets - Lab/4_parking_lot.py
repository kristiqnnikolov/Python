# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot
# On the first line, you will receive the number of commands - N.
# On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}".
# The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot.
# Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
# Note: The order in which we print the result does not matter.

car_numbers = set()

for none in range(int(input())):
    action, number = input().split(", ")
    if action == 'IN':
        car_numbers.add(number)
    elif action == 'OUT':
        if number in car_numbers:
            car_numbers.discard(number)

if car_numbers:
    print("\n".join(car_numbers))
else:
    print("Parking Lot is Empty")
