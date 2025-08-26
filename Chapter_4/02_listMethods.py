list = ["Aman", "Delhi", 56, 89.33, "Banana" , "Varansi"]
print(list)
# methods used on list 
#1 append("value")

list.append("Mumbai")
print(list)

#2 reverse() :->

list.reverse()
print(list)

#3 sort()

l1 = [34,23,45,56,52,3,6,32,1,54,5,7]
l1.sort()
print(l1) 

#4 inset(idx,"value")
list.insert(3,"Shashi")
print(list)

#5 pop(idx)

value = list.pop(3)
print(list)
print(value)

#6 remove(value)

list.remove("Mumbai")
print(list)