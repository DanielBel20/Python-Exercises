"""counts the number of words that contain the letter: "l" in a given string."""

string = input(str("Enter string: "))
list1 = string.split()
NO_OF_WORDS_WITH_L = 0
for i in list1:
    if "l" in i:
        NO_OF_WORDS_WITH_L = NO_OF_WORDS_WITH_L + 1
print(NO_OF_WORDS_WITH_L)
