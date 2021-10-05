import sys
mylist1 = list() # this is the one of the way where we can create a empty list
print(type(mylist1))
mylist = [1,2,3,4,5]
print(mylist)

#Slicing Operation
print(mylist[0:]) # Starting to the End
print(mylist[:5]) #Starting upto specified index 
print(mylist[0:6])  #From specified starting index to specified ending index  
print(mylist[::-1]) # Printitng the reversea a string
print(mylist[0:-1:2]) # printing staring to the end with gap of 2 

#List Function
mylist.append(6)
print("After append function: ", mylist)
mylist.insert(0,0)
print("After insert function: ", mylist)
mylist.remove(0)
print("after removing the 0th index element: ",mylist)
mylist.pop()
print("After popped the last elemnt: ",mylist)
mylist.reverse()
print("After reversing the List: ", mylist)
mylist.sort()
print("After calling the sort function: ",mylist)


#memory allocation

mylist = [10,20,[30,10]]
print('Printing the Id of each elemnet: ')
print(id(mylist[0]))
print(id(mylist[1]))
print(id(mylist[2][0]))
print(id(mylist[2][1]))
print("After modification of List**")
mylist[2][0] = 20
print(mylist)
print(id(mylist[0]))
print(id(mylist[1]))
print(id(mylist[2][0]))
print(id(mylist[2][1]))


# mylist = [1]
print("Size of list: ")
print(sys.getsizeof(mylist1))
mylist1.append(1)
print(mylist1)
print(sys.getsizeof(mylist1))
mylist1.append(2)
print(mylist1)
print(sys.getsizeof(mylist1))
mylist1.append(3)
print(mylist1)
print(sys.getsizeof(mylist1))

List = list()
print(sys.getsizeof(List))
for i in range(1,6):
    List.append(i)
print(List)
print(sys.getsizeof(List))

# Creating Multidimensional List
matrix = list()
row = 3
column = 3
for i in range(row):
    myList = list()
    for j in range(column):
        myList.append(int(input("Enter the Element: ")))
    matrix.append(myList)
print("matrix is:")
for i in range(0,row):
    for j in range(0, column):
        print(matrix[i][j], end=" ")
    print()
