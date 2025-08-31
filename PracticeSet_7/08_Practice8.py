# WAP to print reverse multiplication of a number using for loop

n = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{n}*{11-i} = {n*(11-i)}")
