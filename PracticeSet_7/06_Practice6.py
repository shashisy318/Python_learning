# WAP to print 
#    *
#   ***
#  *****

n = int(input("Enter the no. of level you want : "))

i = 0

while(i<n):
    j =n-i-1
    while(j>0):
        print(" ", end ="")
        j -= 1
    k = 2*i+1
    while(k >0):
        print("*", end ="")
        k -= 1
    print("\n")
    i +=1


# Alternate method ->


for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1), end ="")
    print("\n")