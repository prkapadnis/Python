# Given an array nums containing n distinct numbers in the range [0, n], return the only 
# number in the range that is missing from the array.

def missingNumber(arr):
    # sort the array
    i = 0
    while i < len(arr):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    # Search for the element
    # Case 1
    for index in range(len(arr)):
        if arr[index] != index:
            return index
    # Case 2 
    return len(arr)

nums = [3,0,1]
print(missingNumber(nums))