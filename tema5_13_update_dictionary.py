"""Given a map of food keys and topping values, modify and return the map as follows:
if the key "ice cream" is present, set its value to "cherry".
In all cases, set the key "bread" to have the value "butter".
{"ice cream": "peanuts"} → {"ice cream": "cherry", "bread": "butter"}
{} → {"bread": "butter"}
{"pancake": "syrup"} → {"pancake": "syrup", "bread": "butter"}"""

food = {"ice cream": "peanuts"}
food.update({'bread': "butter"})
if "ice cream" in food.keys():
    food.update({'ice cream': "cherry"})
print(food)
