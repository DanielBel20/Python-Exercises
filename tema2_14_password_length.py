"""Password checker script
#Define a username getting input from the console
#Define a password getting input from the console
#Display the following message ‘The password for user Paul is
#********* is 9 characters long)"""

username = input("Username:")
password = input("Password:")
print('The password for user', username, 'is', ('*'*len(password)), 'is', len(password),
      'characters long')
