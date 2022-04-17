"""We'll say a number is special if it is a multiple of 11 or if it is one more
than a multiple of 11. Return true if the given non-negative number is special."""

number = int(input("Enter number: "))
if number % 11 == 0 or number % 11 == 1:
    print(True, "The number is special!")
else:
    print("The number is usual!")
