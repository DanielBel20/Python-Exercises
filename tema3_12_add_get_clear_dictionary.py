"""Add 2 to the son's height."""

dictionary = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
print(dictionary.get("son's height"))
dictionary["son's height"] = dictionary["son's height"] + 2
print(dictionary)

#Using .get() method print the value of "son's eyes".
print(dictionary.get("son's eyes"))

#clear the dictionary here then print it.
dictionary.clear()
print(dictionary)
