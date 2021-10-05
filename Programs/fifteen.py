"""
    Shuffle the Array
"""
def shuffle(myList, num):
    i = 0
    li = []
    j = num
    while i < num and j < 2*num:
        li.append(myList[i])
        li.append(myList[j])
        i+=1
        j+=1
    return li

myList = [2,3,4,5,6,7]
myList = shuffle(myList, 3)
print(myList)