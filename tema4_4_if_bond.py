"""Write an if statement that asks for the user's name via input() function.
If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print
"Good morning NAME". (Replace Name with user's name)"""

username = input("Please enter your name here: ")
if username == "Bond":
    print("Welcome on board 007!")
else:
    print("Good morning", username + "!")
