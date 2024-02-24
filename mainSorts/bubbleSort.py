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


