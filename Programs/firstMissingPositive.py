def firstMissingPositive(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    
    for index in range(len(arr)):
        if arr[index] != index + 1:
            return index + 1
    return len(arr) + 1

arr = [1]
print(firstMissingPositive(arr))