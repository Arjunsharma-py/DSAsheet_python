def rotateArray(arr, n):
    temp = arr[n-1]
    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr


print(rotateArray([4, 5, 2, 6, 2], 5))
