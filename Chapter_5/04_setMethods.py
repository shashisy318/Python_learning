s = set()

# add() : add element at the end of the set

s.add(10)
s.add(20)
print(s)

# len(s) : gives length of the set

print(len(s))

# remove(ele) : remove "ele" from the set

s.remove(20)
print(s)

# clear() : empties the set 

s.clear()
print(s)

s.add(10)
s.add(40)
s.add(60)
s.add(15)
print(s)

# s1.union(s2) : return a new set with all element from both set

s1 = s.union({4,67,23,10})
print(s1)

# s1.intersection(s2) : return a new set with only element in both set

s2 = s.intersection({4,67,23,10})
print(s2)