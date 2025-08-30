# Conditionals
'''In programming we want to do something if the required conditions 
, meets and for those conditions, conditionals are used'''

mark = int(input("Enter your marks : "))

if(mark>60):
    print("You are Pass.")
elif(mark>33 and mark<60):
    print("You are pass with low marks.")
else:
    print("You are Fail.")

