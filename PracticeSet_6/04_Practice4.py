# Wap to check whether given username contains less than 10 characters or not

username = input("Enter your username : ")

if(len(username) <= 10):
    print("Valid username")
else :
    print("Invalid username")