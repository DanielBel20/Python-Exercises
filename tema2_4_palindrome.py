"""Check if a word is a palindrome. (Use assert for checking)"""

word = input("Enter your word here:")
reversed_Word = word[::-1]
assert word == reversed_Word, "The word " + word + " is not a palindrome"
print("The word", word, "is a palindrome")
