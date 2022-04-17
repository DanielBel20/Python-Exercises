"""Print sum of the numbers between 20 and 100"""
SUM1 = ((100 * 101) / 2) - ((20 * 21) / 2)
print(SUM1)

#sum of the even numbers from the range
SUM1 = 0
for i in range(20, 101):
    if i % 2 == 0:
        SUM1 += i
print(SUM1)
