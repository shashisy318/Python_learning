# if-elif-else these are the keyword used in conditionals to check the conditions
'''there can be only one if and else statement but can be 
any no. of elif statement in a if-else ladder '''  

mark = int(input("Enter your marks : "))

if(mark>=90):
    print("Your Grade is A.")
elif(mark>=80 and mark<90):
    print("Your Grade is B.")
elif(mark>=60 and mark<80):
    print("Your Grade is C.")
elif(mark>=40 and mark<60):
    print("Your Grade is D.")
else:
    print("You are Fail.")

print("End of program")