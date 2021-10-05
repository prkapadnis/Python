"""
Program to change first and last element in list
"""

def Myfunc(myList):
    """
    Program to change first and last element in list
    """
    myList[0], myList[-1] = myList[-1], myList[0]
    return myList

input_list = [1,2,3,4,5]
print(Myfunc(input_list))