"""
    Program to find second most maximum and minimum element in List
"""
def maximum(myList):
    """
        return second max element in list
    """
    myList.remove(max(myList))
    return max(myList)


def minimum(myList):
    """
        Return second min element in List
    """
    myList.remove(min(myList))
    return min(myList)

myList = [10,20,30,40,50]
print(maximum(myList.copy()))
print(myList)
print(minimum(myList.copy()))
print(myList)