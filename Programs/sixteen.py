"""
    Running sum of an array
"""
def runningSum(nums):
    sum = 0
    j = 0
    for i in nums:
        sum += i
        nums[j] = sum
        j += 1
    return nums

def runningSum_1(nums):         #efficient way
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

myList = [1,2,3,4]
print(myList)
myList = runningSum(myList)
print(myList)
myList = runningSum_1(myList)
print(myList)
