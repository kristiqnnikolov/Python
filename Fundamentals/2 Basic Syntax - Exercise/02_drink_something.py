# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives an age and prints what they drink.

# Rules:
# - A kid is defined as someone under or at the age of 14.
# - A teen is defined as someone under or at the age of 18.
# - A young adult is defined as someone under or at the age of 21.
# - An adult is defined as someone above the age of 21.

# Note: All the values are inclusive except the last one!

age = int(input())
if age < 14:
    print(f"drink toddy")
elif age < 18:
    print(f"drink coke")
elif age <= 21:
    print(f"drink beer")
else:
    print(f"drink whisky")
