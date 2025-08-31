# WAP to print multiplication table of a number

n = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{n}*{i} = {n*i}")


# By while loop

i = 1
while(i<=10):
    print(f"{n}*{i} = {n*i}")
    i += 1