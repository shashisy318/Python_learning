# Break : it is used to exit the loop when strikes during the execution

for i in range(10):
    print(i)
    if(i==5): break

'''Output:
0
1
2
3
4
5
'''

# Continue : it is used to skip the particular iteration of the loop when strikes

for i in range(5):
    if(i==3): continue
    print(i)

'''Output: 
0
1
2
4
5
'''

# Pass : it is used to do nothing, sometimes while coding we dont have 
# to do right now but we know that there can be something in future 
# so in those cases we use pass to skip that for now

for i in range(10):
    pass