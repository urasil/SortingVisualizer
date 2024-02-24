# All the sorting algorithms


def bubble_sort(values):
    sorted = values.copy()
    sorted.sort()
    n = len(values)
    arrs = [values.copy()]
    highlightIndexs = [(0, 1)]

    for i in range(n):
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                if values != sorted:
                    arrs.append(values.copy())
                    highlightIndexs.append((j, j+1))
    arrs.append(sorted)
    highlightIndexs.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    return arrs, highlightIndexs


def selection_sort(values):
    sorted = values.copy()
    sorted.sort()
    n = len(values)
    arrs = [values.copy()]
    highlightIndexs = [(0, 1)]

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
        if values != sorted:
            arrs.append(values.copy())
            highlightIndexs.append((i, min_index))
    arrs.append(sorted)
    highlightIndexs.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    return arrs, highlightIndexs


def insertion_sort(values):
    sorted = values.copy()
    sorted.sort()
    arrs = [values.copy()]
    highlightIndexs = [(0, 1)]
    n = len(values)
    for i in range(1, n):
        j = i
        while j > 0 and values[j - 1] > values[j]:
            # visualise swap
            values[j], values[j - 1] = values[j - 1], values[j]
            j -= 1
            if values != sorted:
                arrs.append(values.copy())
                highlightIndexs.append((j, j - 1))
    arrs.append(sorted)
    highlightIndexs.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    return arrs, highlightIndexs


def merge_sort(arr):
    sorted = arr.copy()
    sorted.sort()
    arrs = [arr.copy()]
    highlightIndexs = [(0, 1)]
    n = len(arr)
    size = 1
    while size < n:
        for i in range(0, n, 2 * size):
            left = arr[i: i + size]
            right = arr[i + size: i + 2 * size]
            merged = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            merged += left[l:]
            merged += right[r:]
            arr[i: i + len(merged)] = merged
            if arr != sorted:
                arrs.append(arr.copy())
                highlightIndexs.append((i + l, i + r))
        size *= 2
    arrs.append(sorted)
    highlightIndexs.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    return arrs, highlightIndexs


def quick_sort(arr):
    def partition(arr, low, high):
        i = low
        j = high + 1
        pivot = arr[low]
        while True:
            i += 1
            while arr[i] < pivot:
                if i == high:
                    break
                i += 1
            j -= 1
            while arr[j] > pivot:
                if j == low:
                    break
                j -= 1

            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            if arr != sorted:
                arrs.append(arr.copy())
                highlightIndexs.append((i, j))


        arr[low], arr[j] = arr[j], arr[low]
        if arr != sorted:
            arrs.append(arr.copy())
            highlightIndexs.append((low, j))
        return j

    def sort(arr, low, high):
        if low < high:
            j = partition(arr, low, high)
            sort(arr, low, j - 1)
            sort(arr, j + 1, high)

    sorted = arr.copy()
    sorted.sort()
    arrs = [arr.copy()]
    highlightIndexs = [(0, 1)]
    n = len(arr)
    sort(arr, 0, n-1)
    sort(arr, 0, n - 1)
    arrs.append(sorted)
    highlightIndexs.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    return arrs, highlightIndexs


def heap_sort(values):
    def sift_down(start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and values[child] < values[child + 1]:
                child += 1
            if values[root] < values[child]:
                values[root], values[child] = values[child], values[root]
                if values != sorted:
                    arrs.append(values.copy())
                    highlightIndexs.append((root, child))
                root = child
            else:
                break

    sorted = values.copy()
    sorted.sort()
    arrs = [values.copy()]
    highlightIndexs = [(0, 1)]
    end = len(values) - 1
    start = (end - 1) // 2
    for i in range(start, -1, -1):
        sift_down(i, end)
    for i in range(end, 0, -1):
        values[i], values[0] = values[0], values[i]
        if values != sorted:
            arrs.append(values.copy())
            highlightIndexs.append((i, 0))
        sift_down(0, i - 1)
    arrs.append(sorted)
    highlightIndexs.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    return arrs, highlightIndexs



# VALUES = [10, 3, 1, 9, 8, 6, 7, 2, 4, 5]
# ta = heap_sort(VALUES)
# print(ta)