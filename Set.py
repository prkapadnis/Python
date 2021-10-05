myset = set()
print(type(myset))
myset = {1,2,3,4,5}
print(myset)

#built in function
myset.add(2)# This does not made any change because set don't allow the duplicate values 
print(myset) 
myset.remove(2)
print("After removing 2:", myset)
# print("Using pop() function: ",myset.pop())
print(myset)
second_set = {3,4,5,6}
unioun_set = myset.union(second_set)
print("The Union of set is:",unioun_set)
print("The Intersection of set is:", myset.intersection(second_set))
print("The Difference of set is:", myset.difference(second_set))
print("The Symmetric Difference of set is:", myset.symmetric_difference(second_set))

