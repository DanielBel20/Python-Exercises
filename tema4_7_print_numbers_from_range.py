"""Write an algorithm to print from 1 to 10.
print all multiples of 5 between 1 and 100 (including both 1 and 100).
read three numbers and writes them all in sorted order."""

number = list(range(1, 11))
print(number)

number = list(range(1, 101))
print(number[0], number[4:101:5])

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= b <= a:
    print(c, b, a)
elif c <= a <= b:
    print(c, a, b)

# or
if a > b:
    if c > a:
        print(b, a, c)
    elif b > c:
        print(c, b, a)
    else:
        print(b, c, a)
elif b < c:
    print(a, b, c)
elif a > c:
    print(c, a, b)
else:
    print(a, c, b)

# or
list1 = [a, b, c]
for i in (0, 1):
    for j in (i+1, 2):
        if list1[i] > list1[j]:
            aux = list1[i]
            list1[i] = list1[j]
            list1[j] = aux
print(list1)

# or
list1 = [a, b, c]
list1.sort()
print(list1)
