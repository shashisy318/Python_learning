# Loops :-> 
''' Loops are used to optimize or automate the code where we need to 
excecute a block of code too many times.'''
'''The loop is given with a condition and it keeps repeating 
untill the given condition meets'''

# For example : to print numbers from 1 to 100 we dont write manually instead we use loops

for i in range(1,101) :
    print(i)

# Primarily there are two loops in python 
'''
1. for loop :

syntax :-> for ele in list:
                #statement

'''
# example ->
for i in range(1,6):
    print(i)

'''Output:
1
2
3
4
5
'''


'''
2. while loop :

syntax :->  while(condition):
                #statement

'''

#example ->

i = 1
while(i<6):
    print(i)
    i+=1

'''Output:
1
2
3
4
5
'''