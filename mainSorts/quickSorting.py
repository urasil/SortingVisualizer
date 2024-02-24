#QuickSorting Algorithm
import random

def partition(arr, low, high):
    i = low 
    j = high + 1
    pivot = arr[low]
    while(True):
        i += 1
        while(arr[i] < pivot):
            if i == high:
                break
            i += 1
        j -= 1
        while(arr[j] > pivot):
            if j == low:
                break
            j -= 1

        if i >= j:
            break
        (arr[i], arr[j]) = (arr[j], arr[i])
        #visualise swap

    (arr[low], arr[j]) = (arr[j], arr[low])
    #visualise swap
    return j

def sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        sort(arr, low, j-1)
        sort(arr, j + 1, high)

def quickSort(arr):
    random.shuffle(arr)
    length = len(arr)
    sort(arr, 0, length-1)
    return arr

array = [1,5,3,3,5,7,8,9,1]
print(quickSort(array))





