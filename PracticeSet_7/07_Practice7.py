# WAP to print 
#   ***
#   * *
#   ***

n = int(input("Enter the no. of level you want : "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n , end ="")
    else:
        print("*" , end ="")
        print(" "*(n-2), end="")
        print("*" , end ="")
    print("\n")