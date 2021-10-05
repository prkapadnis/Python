"""
    Given a two strings a and b return True if you can swap two letters in a so the result is
    equal to b otherwise return false
"""
first = "ab"
second = "ba"
new_first = first[2::-1]
print(new_first)
if new_first == second:
    print(True)
