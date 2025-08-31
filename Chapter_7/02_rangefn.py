# Range Function :
# it is used to generate a sequence of number 
# we can also specify start, stop, and step-size as follows :

# range(start, stop, step_size)
# By default start in range is from 0 and step-size is 1


# Example -> 
sum =0
for ele in range(2, 10, 2):
    print(ele)
    sum += ele
print(sum)


s = "School"
for i in s:
    print(i)