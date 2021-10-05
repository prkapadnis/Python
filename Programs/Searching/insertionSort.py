def insertionSort(arr):
    for i in range(len(arr)):
       elementToSort = arr[i]
       while arr[i - 1] > elementToSort and i > 0:
           arr[i], arr[i-1] = arr[i-1], arr[i]
           i -= 1
    return arr


arr = [5,2,3,4,1]
print(insertionSort(arr))
print(arr)