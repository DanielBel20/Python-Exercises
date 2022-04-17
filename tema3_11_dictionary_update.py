"""Print When was Plato born?
Change Plato's birth year from B.C. 427 to B.C. 428."""

dictionary = {"name": "Plato", "country": "Ancient Greece", "born": -427,
              "teacher": "Socrates", "student": "Aristotle"}
print("Plato was born in:", dictionary.get("born"))

dictionary.update({"born": -428})
print(dictionary)
