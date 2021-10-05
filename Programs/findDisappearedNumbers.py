# Given an array nums of n integers where nums[i] is in the range [1, n], return an array 
# of all the integers in the range [1, n] that do not appear in nums.
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def findDisapperedNumber(arr):
    i = 0
    ans = list()
    while i < len(arr):
        correctIndex = arr[i] - 1
        if arr[i] != arr[correctIndex]:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
            i += 1
    for i in range(len(arr)):
        if arr[i] != i + 1:
            ans.append(i+1)
    return ans

nums = [4,3,2,7,8,2,3,1]
print(findDisapperedNumber(nums))
# print(nums)
