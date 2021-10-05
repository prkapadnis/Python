"""
    The Map Function iterates through all the items in the given iterable nad executes the 
    function we pass as an argument to the map function
"""
number = [1,2,3,4,5]
squre = list(map(lambda x : x*x, number))
# print(squre)

number_str = ["1", "2", "3", "4", "5"]
number_int = list(map(lambda x : int(x), number_str))
# print(number_int)

#printing the squre and cube

square = lambda x : x * x 
cube = lambda x : x * x * x
func = [square, cube]
for i in range(6):
    val = list(map(lambda x : x(i), func))
    print(i," = ", val)


# printing Greater than 5
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_greater_5 = lambda x : x > 5
greater_than_5 = list(filter(is_greater_5, num))
print(greater_than_5)