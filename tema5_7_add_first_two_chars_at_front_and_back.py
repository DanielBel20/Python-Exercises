""" Given a string, take the first 2 chars and return the string with the
2 chars added at both the front and back, so "kitten" yields"kikittenki".
If the string length is less than 2, use whatever chars are there.
# "kitten" → "kikittenki"
# "Ha" → "HaHaHa"
# "abc" → "ababcab" """

str1 = input("Enter string:")
str1 = str1[0:2]+str1+str1[0:2]
print(str1)
