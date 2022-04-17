"""Return the sum of the numbers in the array, except ignore sections of numbers divided by 6
[1, 2, 2] → 5
[1, 2, 2, 6, 99, 99, 7] → 210
[1, 1, 6, 7, 2] → 11"""

str1 = [1, 1, 6, 7, 2]
SUM1 = 0
for i in str1:
    if i % 6 != 0:
        SUM1 = SUM1+i
print(SUM1)
