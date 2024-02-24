#Merge Sort Algorithm
def merge(arr, aux, low, mid, high):
    #left and right arrays are already sorted
    aux = array.copy()
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

def sort(arr, aux, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    sort(arr, aux, low, mid)
    sort(arr, aux, mid+1, high)
    merge(arr, aux, low, mid, high)

def mergeSort(arr):
    length = len(arr)
    auxArray = [] *(length-1)
    sort(array, auxArray, 0, length-1)
    return arr


array = [1,5,3,3,5,7,8,9,1]
print(mergeSort(array))


