# WAP to print factorial of a number 

m = int(input("Enter the number : "))
n = m
fact = 1

while(n>0):
    fact *= n 
    n -= 1

print(f"Factorial of {m} is =", fact)