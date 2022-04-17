"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""

mark = int(input("Enter mark: "))
if mark < 25:
    print("The grade is F")
elif mark < 46:
    print("The grade is E")
elif mark in range(46, 51):
    print("The grade is D")
elif mark in range(51, 61):
    print("The grade is C")
elif mark in range(61, 81):
    print("The grade is B")
elif mark > 80:
    print("The grade is A")
