# Recursion :->
''' It is a function which calls itself.'''

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

n = int(input("Enter a number : "))
print(f"The factorial of {n} is {fact(n)}")


# never forget to give base case 
# because that's where function stops calling itself
