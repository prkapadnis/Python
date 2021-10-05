from os import EX_DATAERR


print("Question 1")
for i in range(1, 6):
    for j in range(1,6):
        print(i, end=" ")
    print()

# output:
    # 1 1 1 1 1
    # 2 2 2 2 2
    # 3 3 3 3 3 
    # 4 4 4 4 4
    # 5 5 5 5 5

print("Question 2")

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# output:
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5

print("Question 3")

for i in range(1,6):
    for j in range(1, i+1):
        print('*', end=" ")
    print()

# output:
#     *
#     **
#     ***
#     ****
#     *****

print("Question 4")

for i in range(5, 0, -1):
    for j in range(1,i+1):
        print("*", end="")
    print()

# output:
#     *****
#     ****
#     ***
#     **
#     *

print("Question 5")

for i in range(1,6):
    for j in range(1, i+1):
        print('*', end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1,i+1):
        print('*', end=" ")
    print()

# output:
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

print("Question 7")

for row in range(0, 5):
    totalspace = 5 - row
    for space in range(0, totalspace+1):
        print(" ", end="")
    for col in range(0, row+1):
        print("*", end=" ")
    print()

# output: 
#          *
#         * *
#        * * *
#       * * * *
#      * * * * *

print("Question 8")

for row in range(0, 6):
    totalspace = 6 - row
    for space in range(0, totalspace+1):
        print(" ", end=" ")
    for col in range(row, 0, -1):
        print(col, end=" ")
    for col in range(2, row+1):
        print(col, end=" ")
    print()

# output:
#             1
#           2 1 2
#         3 2 1 2 3
#       4 3 2 1 2 3 4
#     5 4 3 2 1 2 3 4 5