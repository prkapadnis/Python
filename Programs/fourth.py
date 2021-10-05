"""
    Program to print even or odd number in list
"""
def evenOdd(myList):
    """
        Return even and odd number in list
    """
    even = list(filter(lambda x : x%2 == 0, myList))
    print(even)
    odd = list(filter(lambda x : x%2 != 0, myList))
    print(odd)


myList   = [1,2,3,4,5,6,7,8,9,10]
evenOdd(myList)