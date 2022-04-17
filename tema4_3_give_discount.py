"""A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity"""

quantity = int(input("Input quantity: "))
discount = (10*quantity) / 100
if quantity > 1000:
    print("You get 10% discount! So the final price is:", quantity - discount)
else:
    print("Thank you for shopping with us!")
