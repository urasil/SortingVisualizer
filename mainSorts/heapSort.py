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
    n = len(arr)
    heapConstruction(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sink(arr, 0, i)
    return arr

array = [9, 7, 8, 5, 3, 5, 3, 1, 1]
sorted_array = heapSort(array)
print(sorted_array)


