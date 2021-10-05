# """
# The filter() function takes a function which returns a boolean value and then passs each element
# in the iterable through the function and forms the list contains only element which satisfy the 
# condition of function we passed 
# """
marks = [75,74,80,79,67,65,73,69,70,79]
is_greater_75 = lambda x : x > 75
greater_75 = list(filter(is_greater_75, marks))
print(greater_75)   #It prints the element which is greater than 75


fruits = ["Apple", "Banana", "Apricot", "Mango", "Pineapple"]
is_start_with_A = lambda x : x[0] == "A"
start_with_A = list(filter(is_start_with_A, fruits))
print(start_with_A)

nums = [1,2,3,4,5,6,7,8,9,10]
myList = list(filter(lambda x : x%2 == 0, nums))
print(myList)


a_list = list(filter(lambda x: x % 9 == 0, range(1,1001)))
print(a_list)