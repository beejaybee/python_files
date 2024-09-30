
"""
Write a program that ask for username and password
if the username and password is correct, print 'Welcome, It's nice to meet you, username'.
if the username and password is not correct, print 'You've entered wrong username and password'"
"""

print("what is your username")

username = input()

print('What is your password?')

password = input()

if username == "inspectorbeejay" and password == "Sergentbeejay":
    print("It is nice to meet you " + username)
else :
    print("You have entered the wrong username or password")

