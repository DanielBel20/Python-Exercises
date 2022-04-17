"""Given an array of ints, return the sum of the first 2 elements in the array.
If the array length is less than 2, just sum up the elements that exist,
returning 0 if the array is length 0.
[1, 2, 3] → 3
[1, 1] → 2
[1, 1, 1, 1] → 2"""

STR1 = [1, 1, 1, 1]
if len(STR1) == 1:
    print(STR1[0]+STR1[0])
elif len(STR1) == 0:
    print("0")
else:
    STR1 = STR1[0]+STR1[1]
    print(STR1)
