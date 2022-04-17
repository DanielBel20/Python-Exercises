""" Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. For 'eu merg la mare' the program must display 'eure' """

string_1 = input("Enter the string: ")
string_2 = string_1[:2]
string_3 = string_1[-2:]
print("The string made of the first 2 and the last 2 chars is: "+string_2 + string_3)
