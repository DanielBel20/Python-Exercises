"""Modify and return the given dictionary as follows: if the key "a" has a value, set the key "b"
to have that same value.
In all cases remove the key "c", leaving the rest of the dictionary unchanged.
{"b": "bbb", "c": "ccc", "a": "aaa"} → {"b": "aaa", "a": "aaa"}
{"b": "xyz", "c": "ccc"} → {"b": "xyz"}
{"d": "hi", "c": "meh", "a": "aaa"} → {"d": "hi", "b": "aaa", "a": "aaa"}"""

dictionary1 = {"b": "bbb", "c": "ccc", "a": "aaa"}
dictionary2 = {"b": "xyz", "c": "ccc"}
dictionary3 = {"d": "hi", "c": "meh", "a": "aaa"}
while "c" in dictionary1 and "c" in dictionary2 and "c" in dictionary3:
    dictionary1.pop("c")
    dictionary2.pop("c")
    dictionary3.pop("c")
    if "c" not in dictionary1 and "c" not in dictionary2 and "c" not in dictionary3:
        print(dictionary1)
        print(dictionary2)
        print(dictionary3)
if "a" in dictionary1 and "b" in dictionary1:
    dictionary1.update({'b': dictionary1["a"]})
    if "a" in dictionary2 and "b" in dictionary2:
        dictionary1.update({'b': dictionary1["a"]})
        if "a" in dictionary3 and "b" in dictionary3:
            dictionary1.update({'b': dictionary1["a"]})
print(dictionary1)
print(dictionary2)
print(dictionary3)
