""" Write a Python program to check the validity of password input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters. """


def fun_pass(passw):
    """function for password checking"""
    if any(letter.isalpha() for letter in passw) and any(letter.isdigit() for
            letter in passw) and any(letter.isupper() for letter in passw) and \
            any(letter.islower() for letter in passw) and len(passw) in range(6, 17):
        print("Your password is valid!")
    else:
        print("Your password is invalid!")


passwo = input("Enter password:")

fun_pass(passwo)

# or
password = input("Enter password: ")
HAS_SMALL_LETTER = False
HAS_NUMBER = False
HAS_CAPITAL_LETTER = False
HAS_SYMBOL = False
for i in password:
    if i.isnumeric():
        HAS_NUMBER = True
    if i.isupper():
        HAS_CAPITAL_LETTER = True
    if i.islower():
        HAS_SMALL_LETTER = True
    if i in ["$", "#", "@"]:
        HAS_SYMBOL = True
if HAS_NUMBER and HAS_SYMBOL and HAS_SMALL_LETTER and HAS_CAPITAL_LETTER \
        and len(password) in range(6, 17):
    print("Your password is valid!")

# or
password = input("Enter password: ")
HAS_SMALL_LETTER = 0
HAS_NUMBER = 0
HAS_CAPITAL_LETTER = 0
HAS_SYMBOL = 0
for j in password:
    if j.isdigit():
        HAS_NUMBER += 1
    if j.isupper():
        HAS_CAPITAL_LETTER += 1
    if j.islower():
        HAS_SMALL_LETTER += 1
    if j.isalpha():
        HAS_SYMBOL += 1
if HAS_NUMBER == 0:
    print("Your password must contain at least 1 digit")
if HAS_CAPITAL_LETTER == 0:
    print("Your password must contain at least 1 upper case")
if HAS_SMALL_LETTER == 0:
    print("Your password must contain at least 1 lower case")
if HAS_SYMBOL == 0:
    print("Your password must contain at least 1 symbol")
if len(password) < 6:
    print("Your password does not match the minimum length required")
if len(password) > 16:
    print("Your password does not match the maximum length required")
if (HAS_NUMBER and HAS_CAPITAL_LETTER and HAS_SMALL_LETTER and HAS_SYMBOL) > 0 \
        and len(password) in range(6, 17):
    print("Your password is valid!")
