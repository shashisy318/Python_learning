# WAP to store four fruits in a list entered by user

list = []

f1 = input("Enter the fruit name : ")
list.append(f1)
f2 = input("Enter the fruit name : ")
list.append(f2)
f3 = input("Enter the fruit name : ")
list.append(f3)
f4 = input("Enter the fruit name : ")
list.append(f4)

list.sort()
print(list)