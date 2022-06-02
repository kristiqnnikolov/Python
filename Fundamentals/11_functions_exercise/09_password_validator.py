# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"


def password(text):
    password_is_valid = True
    numbers = '0 1 2 3 4 5 6 7 8 9'
    letters = 'a b c d e f g h i j k l m no p q r s t u v w x y z '
    alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    if not 6 <= len(text) <= 10:
        password_is_valid = False
        print(f"Password must be between 6 and 10 characters")

    for letter in text:
        if letter not in letters and letter not in numbers and letter not in alpha:
            print(f"Password must consist only of letters and digits")
            password_is_valid = False
            break

    counter = 0
    for number in text:
        if number in numbers:
            counter += 1
    if counter <= 1:
        print(f"Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        print(f"Password is valid")


txt = input()
password(txt)
