# Given an array of integers nums containing n + 1 integers where each integer is in the range 
# [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra 
# space.

def findDuplicateNumber(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else :
            i += 1
    
    for index in range(len(arr)):
        if arr[index] != index + 1:
            return arr[index]

nums = [3,1,3,4,2]
print(findDuplicateNumber(nums))
