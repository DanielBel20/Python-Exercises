""" Write a method with a while loop to prints 1 through n in square brackets. For example, if n = 6 print [1] [2] [3] [4] [5] [6]
Print: (input max number of asterisks from the keyboard)
*
**
***
****
*****"""

n = int(input("Enter a number:"))
i = 0
while i in range(n):
    i = i+1
    print([i])
    print('*'*i)
# or
n = int(input("Enter a number:"))
while i < n:
    print(i*"*")
    i += 1

# or
for i in range(0, n+1):
    print('*'*i)
