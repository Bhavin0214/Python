username = input("enter your username here: ")

if len(username)<10:
    print("enter valid username, must have 10 characters.")
else:
    print("hello",username)