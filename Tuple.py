mytuple = tuple()
mytuple = (5,4,3,2,1)
print(mytuple.__sizeof__())
print(mytuple)
print(type(mytuple))
print("The length of Tuple: ", mytuple.__len__())
print(mytuple.__sizeof__())
print(tuple(sorted(mytuple))) # It returns a list after sorting and it creates a new tuple
print(mytuple)