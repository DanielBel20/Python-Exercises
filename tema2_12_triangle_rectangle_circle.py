"""Build a program to calculate the followings using the input from the user
triangle area using input
rectangle area and perimeter
circle area"""

# Three sides of the triangle is a, b and c:
a = float(input('Enter first side of the triangle: '))
b = float(input('Enter second side of the triangle: '))
c = float(input('Enter third side of the triangle: '))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)

# Rectangle area
a = float(input('Enter the length of the rectangle: '))
b = float(input('Enter the width of the rectangle: '))
rectangle_area = a * b
rectangle_perimeter = 2 * (a + b)
print('The perimeter of the rectangle is:', rectangle_perimeter)
print('The area of the rectangle  is:', rectangle_area)

# Circle area
r = float(input('Enter the radius of the circle: '))
PI = 3.14
circle_area = PI * r ** 2
print('The area of the circle is:', circle_area)
