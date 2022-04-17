""" Given a string, return a version without the first and last char, so "Hello" yields "ell".
The string length will be at least 2.
"Hello" → "ell"
"java" → "av"
"coding" → "odin" """
str1 = input("Enter string: ")
if len(str1) < 2:
    print("The string must contain at least 2 characters!")
else:
    str1 = str1[1:len(str1)-1]
    print(str1)
