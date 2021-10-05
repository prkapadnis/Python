"""
    finding the k'th largest element in the list
"""

def kth_largest(myList, k):
    if len(myList) < k:
        return "Invalid input"
    # myList = list(set(myList))
    myList.sort()
    return myList[-k]


myList = [3,2,3,1,2,4,5,5,6]
print(kth_largest(myList, 4))