"""Write a Python program that tells a user that the number they entered is not a 5 or a 6."""

number = int(input("Enter your number here: "))
if number not in range(5, 7):
    print("Your number is neither a 5 nor a 6!")
else:
    print("Ciocolata e buna!")
