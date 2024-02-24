#Selection Sort Algorithm
def selectionSort(arr):
    for i in range(len(arr)):
        minValue = min(arr[i:])
        #i added because arr[i:].index() return index relative to slice
        #so there are actually i more elements before the slice
        idx = i + arr[i:].index(minValue)
        if minValue == arr[i]:
            continue
        else:
            #visualise swap
            (arr[i], arr[idx]) = (arr[idx], arr[i])

    return arr

array = [1,5,3,3,5,7,8,9,1]
print(selectionSort(array))

