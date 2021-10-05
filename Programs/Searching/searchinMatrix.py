# Linear Search In Matrix

def linearSearch(matrix, target):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == target:
                return [row, col]
    return False

matrix = [
    [18, 9, 12],
    [36, -4, 91],
    [44, 33, 16],
]
target = 91

# print(linearSearch(matrix, target))

# Binary Search Like Approach OR Optimised Solution 

# Search in Matrix which is sorted in Row wise and column wise
def binarySearch(arr, target):
    row = 0
    col = len(arr[row]) - 1
    while row < len(arr) and col >= 0:
        if arr[row][col] == target:
            return [row, col]
        elif arr[row][col] > target:
            col -= 1
        elif arr[row][col] < target:
            row += 1
    return -1


matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [28, 29, 37, 49],
    [33, 34, 38, 50],
]
target = 15
print(binarySearch(matrix, target))
