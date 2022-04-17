"""Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
ODD = 0
EVEN = 0
for i in numbers:
    if i % 2 == 0:
        EVEN = EVEN+1
    else:
        ODD = ODD+1
print("Number of even numbers: ", EVEN)
print("Number of odd numbers: ", ODD)
