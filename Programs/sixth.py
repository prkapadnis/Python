"""
    Finding the third largest element in the list
"""
def finding_largest_third(myList):
    myList = list(set(myList))
    myList.sort()
    return myList[-3]
        


myList = [2,2,3,1]
print(finding_largest_third(myList))