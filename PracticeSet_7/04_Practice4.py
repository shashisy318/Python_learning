# WAP to print sum of first n natural no.

n = int(input("Enter n : "))
sum = 0
i = 1 
while(i<=n):
    sum += i
    i += 1

print(f"sum of {n} natural number is =" , sum)
