from copy import deepcopy


def __partition(arrays, start, end, index):
    pivot = arrays[index][start]
    low = start + 1
    high = end

    while True:
        while low <= high and arrays[index][high] >= pivot:
            high = high - 1

        while low <= high and arrays[index][low] <= pivot:
            low = low + 1

        if low <= high:
            arrays[index][low], arrays[index][high] = arrays[index][high], arrays[index][low]
            arrays[index+1][low], arrays[index+1][high] = arrays[index+1][high], arrays[index+1][low]
        else:
            break

    arrays[index][start], arrays[index][high] = arrays[index][high], arrays[index][start]
    arrays[index+1][start], arrays[index+1][high] = arrays[index+1][high], arrays[index+1][start]

    return high


def __quickCalc(arrays, start, end, index=0):
    if start >= end:
        return

    p = __partition(arrays, start, end, index)
    __quickCalc(arrays, start, p-1)
    __quickCalc(arrays, p+1, end)
  
        
def quickSort(arrays):
    X = deepcopy(arrays[0])
    y = deepcopy(arrays[1])
    __quickCalc([X, y], 0, len(X)-1)
    return X, y
