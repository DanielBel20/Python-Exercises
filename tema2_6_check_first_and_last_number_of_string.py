"""Check if the first and last number of a string  is the same (input the string from keyboard)"""

string = input("Input a string that contains only numeric digits: ")
#if (string[0] == string[-1]):
    #print("Yes, the first number and last number of this string are the same :)!")
#else:
    #print("No, the first number and last number are not the same :(!")
firstNumber = string[0]
lastNumber = string[-1]
assert firstNumber == lastNumber, "No, the first number and last number are not the same :(!"
print("Yes, the first number and last number of this string are the same :)!")
