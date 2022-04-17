"""Modify and return the given map as follows: for this problem
the map may or may not contain the "a" and "b" keys.
If both keys are present, append their 2 string values together
and store the result under the key "ab".
{"b": "There", "a": "Hi"} → {"b": "There", "a": "Hi", "ab": "HiThere"}
{"a": "Hi"} → {"a": "Hi"}
{"b": "There"} → {"b": "There"}"""
dictionary = {"b": "There", "a": "Hi"}
if "a" in dictionary.keys() and "b" in dictionary.keys():
    dictionary["ab"] = dictionary.get("a") + dictionary.get("b")
print(dictionary)
