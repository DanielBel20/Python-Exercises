"""Given a dictionary of food keys and topping values, modify and return the dictionary as follows:
if the key "potato" has a value, set that as the value for the key "fries". If the key "salad"
has a value, set that as the value for the key "spinach".
{"potato": "ketchup"} → {"potato": "ketchup, "fries": "ketchup"}
{"potato": "butter"} → {"potato": "butter", "fries": "butter"}
{"salad": "oil", "potato": "ketchup"}
→ {"salad": "oil", "fries": "ketchup", "spinach": "oil", "potato": "ketchup"}"""

food1 = {"potato": "ketchup"}
food2 = {"potato": "butter"}
food3 = {"salad": "oil", "potato": "ketchup"}

# n=int(input("Enter a number of elements in the dictionary: "))
# food1 = {}
# for i in range (n):
#     key=input("Enter key :")
#     value=input("Enter values :")
#     food1.update({key: value})
#     print(food1) # Entering the dictionaries from keyboard

if "potato" in food1.keys():
    food1.update({'fries': food1["potato"]})
    print(food1)
if "potato" in food2.keys():
    food2.update({'fries': food2["potato"]})
    print(food2)
if "potato" in food3.keys():
    food3.update({'fries': food3["potato"]})
    print(food3)
if "salad" in food1.keys():
    food1.update({'spinach': food1["salad"]})
    print(food1)
if "salad" in food2.keys():
    food2.update({'spinach': food2["salad"]})
    print(food2)
if "salad" in food3.keys():
    food3.update({'spinach': food3["salad"]})
    print(food3)
