# You have just bought the latest and greatest computer game – Need for Seed III.
# Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain.
# On the next n lines, the cars themselves will follow with their mileage and fuel available,
# separated by "|" in the following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
# •	"Drive : {car} : {distance} : {fuel}":
# o	You need to drive the given distance, and you will need the given fuel to do that.
# If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance,
# decrease its fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if a car's mileage reaches 100 000 km,
# remove it from the collection(s) and print: "Time to sell the {car}!"
# •	"Refuel : {car} : {fuel}":
# o	Refill the tank of your car.
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more
# than you can fit in the tank, take only what is required to fill it up.
# o	Print a message in the following format: "{car} refueled with {fuel} liters"
# •	"Revert : {car} : {kilometers}":
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it
# with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."

num = int(input())
cars = {}
for x in range(num):
    reveal = input().split("|")
    car = reveal[0]
    mileage = int(reveal[1])
    fuel = int(reveal[2])
    if car not in cars:
        cars[car] = {"mileage": mileage, "fuel": fuel}
current_command = input()
while not current_command == 'Stop':
    command = current_command.split(" : ")
    action = command[0]
    car = command[1]
    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if car in cars:
            if cars[car]["fuel"] >= fuel:
                cars[car]["mileage"] += distance
                cars[car]["fuel"] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            else:
                print(f"Not enough fuel to make that ride")
            if cars[car]["mileage"] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")
    elif action == "Refuel":
        fuel = int(command[2])
        if car in cars:
            current = cars[car]["fuel"]
            if cars[car]["fuel"] < 75:
                cars[car]["fuel"] += fuel
                if cars[car]["fuel"] >= 75:
                    cars[car]["fuel"] = 75
                    print(f"{car} refueled with {75 - current} liters")
                else:
                    print(f"{car} refueled with {fuel} liters")
            else:
                print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        km = int(command[2])
        cars[car]["mileage"] -= km
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")
    current_command = input()
for car, attr in cars.items():
    print(f"{car} -> Mileage: {attr['mileage']} kms, Fuel in the tank: {attr['fuel']} lt.")
