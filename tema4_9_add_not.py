"""Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged."""

string = input("Enter string:")
if string[0:3] != "not":
    print("not"+string)
elif string[0:3] == "not":
    print(string)
