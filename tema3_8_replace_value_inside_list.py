"""Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
Only update the first occurrence of a value"""

list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    index = list1.index(20)
    list1[index] = 200
    print(list1)
else:
    print("Unfortunately 20 is not in the list")
