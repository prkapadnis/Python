"""
The reduce() function works by calling the function that we passed for the first two items in
the sequence  and result returned by the function is used with another call to function along
side next element in the function
"""
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]
# we want sum of all elements in the list
sum = reduce(lambda x, y : x + y, numbers)
print("The sun of all elements in list is:",sum)
# Maximum element in the List

maxi = reduce(lambda x,y: x if x > y else y, numbers)
print('The Greatest element in list: ',maxi)