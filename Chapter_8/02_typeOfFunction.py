# Types of function :-
''' 
1 -> Built-in function :

Already present in python.
examples of built-in functions includes len(), print(), range(),etc.

'''
'''
2 -> User defined function  :

These are defined by the user.
the fun() functions we defined is an example of user defined function.

'''

# Function with arguments  :

'''A function can accept some value it can work with. we can put these
values in the parenthesis '''

def greet(name):                      
    print("Good Morning,", name)

greet("Roshan")                           

# Function with return  :

'''A function can also return value as shown in the given example'''

def greet(name):                      
    gt = "Good Morning, " + name
    return gt

gt = greet("Roshan") 
print(gt)