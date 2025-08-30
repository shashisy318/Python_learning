# WAP to detect spam from comment if it has some strings like :
 
c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

comment = input("Enter your comment : ")

if((c1 in comment) or (c2 in comment) or (c3 in comment) or (c4 in comment)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")