# Can wwe have a set with 18(int) and '18'(str)

s = set()
s.add(18)
s.add('18')
print(s)

# Yes, We can store numeric digit in string and integer both uniquely

# but for floating point python treat it as same, let's see with an example :

s.add(18.0)
print(s)

# here we can see that we get length of set as 2 that mean python take 
# 18(int) and 18.0(float)  as same .
