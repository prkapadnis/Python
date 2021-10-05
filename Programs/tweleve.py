"""
    Give an integer n and n spcae separated integers as input create a tuple of these n integers
"""
import builtins
n = int(input())
l1 = [int(input()) for i in range(n)] 
myTuple = tuple(l1)
print(hash(myTuple))