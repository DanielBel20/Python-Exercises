"""Print max and minim from the list"""

lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
lst.sort()
print('min =', lst[0])
print('max =', lst[-1])

#or
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("min= ", min(lst))
print("max= ", max(lst))
