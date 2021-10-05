# Search in Strictly sorted matrix

def binarySearch(arr, target, start, end):
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        if arr[mid] < target:
            start = mid + 1
    return -1


def search(arr, target):
    row = 0
    col = len(arr[row]) - 1
    while row < len(arr):
        if target <= arr[row][-1]:
            return [row, binarySearch(arr[row], target, 0, col)]
        else:
            row += 1
    return False

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# matrix = [[1]]
target = 1
# print(len(matrix[0]))
# print(len(matrix))
# print( 13 in matrix[3])
# print(matrix[2][-1])
print(search(matrix, target))
