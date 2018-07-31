print("Hi, this is a super user gatewway")
username = input("Username: ")

if username != "c4e": 
    print("You're not a super user!")
else:
    password = input("Password: ")
    if password != "codethechange":
        print("Incorrect password")
    else: 
        print("Welcome", username)

