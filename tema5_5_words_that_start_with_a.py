"""returns the number of words that start with letter "a" in a string."""

STR1 = str(input("Enter string:")).split()
NAME_STARTING_WITH_A = 0
for word in STR1:
    if word[0] == "a":
        NAME_STARTING_WITH_A = NAME_STARTING_WITH_A + 1
print(NAME_STARTING_WITH_A)
