"""counts the number of words that contain the letter: "l" in a given string."""

string1 = input(str("Enter string: ")).split()
NO_OF_WORDS_WITH_L = 0
for i in string1:
    if "l" in i:
        NO_OF_WORDS_WITH_L = NO_OF_WORDS_WITH_L + 1
print(NO_OF_WORDS_WITH_L)
