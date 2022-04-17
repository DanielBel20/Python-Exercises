"""Given an array of ints length 3, figure out which is larger between the first
and last elements in the array and set all the other elements to be that value.
Return the changed array.
[1, 2, 3] → [3, 3, 3]
[11, 5, 9] → [11, 11, 11]
[2, 11, 3] → [3, 3, 3]"""

str1 = [1, 2, 3]
if str1[0] >= str1[2]:
    sir = [str1[0], str1[0], str1[0]]
else:
    sir = [str1[2], str1[2], str1[2]]
print(sir)

# or
number_list = [1, 2, 3]
max_number = max(number_list[0], number_list[len(number_list)-1])
for i, n in enumerate(number_list):
    number_list[i] = max_number
print(number_list)
