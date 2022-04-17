"""Remove empty strings from the list of strings"""

string = ["Mike", "", "Emma", "Kelly", "", "Brad"]
N = string.count("")
if N > 0:
    for space in range(N):
        string.remove("")
    print(string)
else:
    print("There is no empty string in the list")

#or
string = ["Mike", "", "Emma", "Kelly", "", "Brad"]
while "" in string:
    string.remove("")
    if "" not in string:
        print(string)

#or
string = ["Mike", "", "Emma", "Kelly", "", "Brad"]
string = list(dict.fromkeys(string))
string.remove("")
print(string)

#or
string = ["Mike", "", "Emma", "Kelly", "", "Brad"]
string1 = list(filter(None, string))
print(string1)
