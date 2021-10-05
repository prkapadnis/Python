"""
    Program to remove multiple elements from a list
"""

def rm_duplicate(myList):
    """
        return a list of unique values
    """
    return list(set(myList))


length = int(input("Enter the length of list:"))
myList = [int(input(f"Enter the value for {num} index:")) for num in range(length)]
print(rm_duplicate(myList))