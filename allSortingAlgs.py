#Bubble Sort Algorithm
def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if j == length-1:
                break
            if arr[j+1] < arr[j]:
                #swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [1,5,3,3,5,7,8,9,1]
print(bubbleSort(array))


# #Heap Sort Algorithm

def sink(arr, i, N):
    while 2*i+1 < N:
        j = 2*i+1
        if j+1 < N and arr[j+1] > arr[j]:
            j += 1
        if arr[i] >= arr[j]:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i = j

def heapConstruction(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        sink(arr, i, n)
    return arr

def heapSort(arr):
    arrs = [arr.copy()]
    n = len(arr)
    heapConstruction(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sink(arr, 0, i)
        arrs.append(arr.copy())
    print(arrs)
    return arr

array = [9, 7, 8, 5, 3, 5, 3, 1, 1]
sorted_array = heapSort(array)
print(sorted_array)



#Insertion Sort Algorithm
def insertionSort(arr):
    arrs = [arr.copy()]
    length = len(arr)
    for i in range(1,length):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            #visualise swap
            (arr[j], arr[j-1]) = (arr[j-1], arr[j])
            j -= 1
            arrs.append(arr.copy())
    print(arrs)
    return arr

array = [1,5,3,3,5,7,8,9,1]
print(insertionSort(array))


#Merge Sort Algorithm
def merge(arr, aux, low, mid, high, arrs):
    #left and right arrays are already sorted
    aux = arr.copy()
    i = low
    j = mid + 1
    for k in range(low, high+1):
        if i > mid:
            #visualise swap
            arr[k] = aux[j]
            j += 1
        elif j > high:
            #visualise swap
            arr[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            #visualise swap
            arr[k] = aux[j]
            j += 1
        else:
            #visualise swap
            arr[k] = aux[i]
            i += 1  
        arrs.append(arr.copy())

def sort(arr, aux, low, high, arrs):
    if low >= high:
        return
    mid = low + (high - low) // 2
    sort(arr, aux, low, mid, arrs)
    sort(arr, aux, mid+1, high, arrs)
    merge(arr, aux, low, mid, high, arrs)

def mergeSort(arr):
    arrs = [arr.copy()]
    length = len(arr)
    auxArray = [] *(length-1)
    sort(array, auxArray, 0, length-1, arrs)
    print(arrs)
    return arr


array = [1,5,3,3,5,7,8,9,1]
print(mergeSort(array))



#QuickSorting Algorithm
import random

def partition(arr, low, high, arrs):
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
        arrs.append(arr.copy())
        #visualise swap

    (arr[low], arr[j]) = (arr[j], arr[low])
    arrs.append(arr.copy())
    #visualise swap
    return j

def sort(arr, low, high, arrs):
    if low < high:
        j = partition(arr, low, high, arrs)
        sort(arr, low, j-1, arrs)
        sort(arr, j + 1, high, arrs)

def quickSort(arr):
    arrs = [arr.copy()]
    random.shuffle(arr)
    length = len(arr)
    sort(arr, 0, length-1, arrs)
    print(arrs)
    return arr

array = [1,5,3,3,5,7,8,9,1]
print(quickSort(array))




#Selection Sort Algorithm
def selectionSort(arr):
    arrs = [arr.copy()]
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
            arrs.append(arr.copy())
    print(arrs)
    return arr

array = [1,5,3,3,5,7,8,9,1]
print(selectionSort(array))

