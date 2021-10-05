"""
    set - Discard, remove , pop function from hackerrank
"""
s = set(map(int, input("Enter the number:").split()))
n = int(input())
for i in range(n):
    cammand = input().split()   #It takes command like remove 9
    if len(cammand) > 1:
        e = int(cammand[1])
    if cammand[0] == "pop":
        s.pop()
    if cammand[0] == "remove":
        s.remove(e)
    if cammand[0] == "discard":
        s.discard(e)
print(sum(s))
