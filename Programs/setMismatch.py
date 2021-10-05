#You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
# in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the 
# form of an array.

def setMismatch(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else :
            i += 1
    
    for index in range(len(arr)):
        if arr[index] != index + 1:
            return [arr[index], index+1]

nums = [1, 1]
print(setMismatch(nums))
