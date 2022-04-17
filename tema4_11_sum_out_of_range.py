"""Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive,
are forbidden, so in that case just return 20."""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
sum1 = a+b
if sum1 in range(10, 20):
    print(20)
else:
    print(sum1)
