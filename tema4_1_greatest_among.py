"""Take two int values from user and print greatest among them"""

number1 = int(input("Insert first number: "))
number2 = int(input("Insert second number: "))
if number1 > number2:
    print("The greatest number is:", number1)
elif number1 < number2:
    print("The greatest number is:", number2)
else:
    print("The numbers are equal!")
