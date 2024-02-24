#Insertion Sort Algorithm
def insertionSort(arr):
    length = len(arr)
    for i in range(1,length):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            #visualise swap
            (arr[j], arr[j-1]) = (arr[j-1], arr[j])
            j -= 1
    return arr

array = [1,5,3,3,5,7,8,9,1]
print(insertionSort(array))


