def display(myList):
    myList.append(6)
    print(myList)
    print(id(myList))

myList = [1,2,3,4,5]
display(myList)
print(myList)
print(id(myList))