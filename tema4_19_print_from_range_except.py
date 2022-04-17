"""Write a Python program that prints all the numbers from 0 to 6 except 3 and 6"""

for i in range(0, 7):
    if i not in (3, 6):
        print(i)
