# Default Parameter :-

''' this tells the function that if i provide some value for the parameter
then use that value.
and if no value is provided for that parameter then take default value given.
Let's see how from the following example :
'''
def greet(name , ending = "Thankyou"):                      
    print("Good Morning,", name)
    print(ending)

greet("Roshan")
'''In this we haven't passed any value for ending 
hence it will take value given by default'''

greet("Shriya", "Thanks")   
'''In this we have passed 'Thanks' for ending 
hence it will take 'Thanks' as a value for 'ending'
'''
