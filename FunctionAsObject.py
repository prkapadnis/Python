def checkOdd(num):
    if num % 2 != 0:
        return True

def changeList(alist, func):
    oddNum = []
    for i in alist:
        if func(i):
            oddNum.append(i)
    return oddNum

a_list = range(1,21)
print(changeList(a_list, checkOdd)) 