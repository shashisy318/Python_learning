# WAP to check prime or not

n = int(input("Enter the number : "))
flag = True
for i in range(2,(n//2)+1) :
    if n%i == 0 :
        print(n,"is not a prime number.")
        flag = False
        break
if(n == 1):
    print("1 is neither prime nor composite")
elif(flag ):
    print(n,"is a prime number.")
