"""Create a list with the names of girls from your group (the names do not have to be distinct).
Following the order, solve the next requirements:
1- Sort the list.
2- Using an auxiliary list, find the number of appearances for each name.
3- Find the name that appears the most in the initial list.
4- Find the name that appears the least in the initial list.
5- Reverse the order of the elements from the initial list."""

list1 = ["alina", "roxana", "maria", "petruta", "maria"]
# 1
list1.sort()
print(list1)

# 2
list2 = [list1.count("alina"), list1.count("roxana"), list1.count("maria"), list1.count("petruta")]
print(list2)
noOfOccurrence = {"alina": list1.count("alina"), "roxana": list1.count("roxana"),
                 "maria": list1.count("maria"), "petruta": list1.count("petruta")}
print(list(noOfOccurrence.values()))
print(noOfOccurrence)

# 3
if list1.count("alina") > list1.count("roxana") and list1.count("alina") > list1.count("maria") \
        and list1.count("alina") > list1.count("petruta"):
    print("Alina appears the most times in the list!")
if list1.count("roxana") > list1.count("alina") and list1.count("roxana") > list1.count("maria") \
        and list1.count("roxana")>list1.count("petruta"):
    print("Roxana appears the most times in the list!")
if list1.count("maria") > list1.count("alina") and list1.count("maria") > list1.count("roxana") \
        and list1.count("maria") > list1.count("petruta"):
    print("Maria appears the most times in the list!")
if list1.count("petruta") > list1.count("alina") and list1.count("petruta") > list1.count("maria") \
        and list1.count("petruta") > list1.count("roxana"):
    print("Petruta appears the most times in the list!")

# 4
if list1.count("alina") <= list1.count("roxana") and list1.count("alina") <= list1.count("maria") \
        and list1.count("alina") <= list1.count("petruta"):
    print("Alina appears the least times in the list!")
if list1.count("roxana") <= list1.count("alina") and list1.count("roxana") <= list1.count("maria") \
        and list1.count("roxana") <= list1.count("petruta"):
    print("Roxana appears the least times in the list!")
if list1.count("maria") <= list1.count("alina") and list1.count("maria") <= list1.count("roxana") \
        and list1.count("maria") <= list1.count("petruta"):
    print("Maria appears the least times in the list!")
if list1.count("petruta") <= list1.count("alina") and list1.count("petruta") <= \
        list1.count("maria") and list1.count("petruta") <= list1.count("roxana"):
    print("Petruta appears the least times in the list!")

# 5
list1 = ["alina", "roxana", "maria", "petruta", "maria"]
print(list1[::-1])
