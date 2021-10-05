"""
    Program to swap two elements in a list
"""
def swap(myList, first, second):
    myList[first] , myList[second] = myList[second], myList[first]
    return myList

first_pos = int(input("Enter the first position:"))
second_pos = int(input("Enter the second Position:"))
myList = [1,2,3,4,5]
print(swap(myList, first_pos, second_pos))