nums = [1,2,3,4,5,6,7,8,9,10]
myList = []

# 1] I want each n in nums
myList = []
for n in nums:
    myList.append(n)
print(myList)
# list Comprehension
myList = [n for n in nums]
print(myList)
myList.clear()
# -----------1]-------------

# 2] I want n in nums if n is even
for n in nums:
    if n % 2 == 0:
        myList.append(n)
print(myList)
myList.clear()
#List Comprehension
myList = [n for n in nums if n % 2 == 0]
print(myList)
myList.clear()
# -----------2]-------------

# 3] I want (letter , num) pair for each letter in 'abcd' and each number in '0123';
for num in range(4):
    for letter in "abcd":
        myList.append((letter, num))
print(myList)
myList.clear()
#List Comprehension
myList = [[letter, num] for letter in "abcd" for num in range(4)]
print(myList)
myList.clear()
# -----------3]-------------

