import tkinter as tk
import time

class SortingCanvas(tk.Canvas):
    def __init__(self, rectangle_color, text_color, master, **kwargs):
        super().__init__(master, **kwargs)
        self.rectangles = []
        self.texts = []
        self.rectangle_color = rectangle_color
        self.text_color = text_color

    def create_rectangles(self, values):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        bar_width = width / len(values)
        for i, value in enumerate(values):
            x0 = i * bar_width
            y0 = height
            x1 = (i + 1) * bar_width
            y1 = height - (value / max(values)) * height
            rectangle = self.create_rectangle(x0, y0, x1, y1, fill=self.rectangle_color)
            self.rectangles.append(rectangle)
            text_x = (x0 + x1) / 2
            text_y = (y0 + y1) / 2
            text = self.create_text(text_x, text_y, text=str(value), fill=self.text_color, font=("Arial", 20))
            self.texts.append(text)

    def update_rectangles(self, values):
        width = self.winfo_width()
        height = self.winfo_height()
        bar_width = width / len(values)
        for i, value in enumerate(values):
            x0 = i * bar_width
            y0 = height
            x1 = (i + 1) * bar_width
            y1 = height - (value / max(values)) * height
            self.coords(self.rectangles[i], x0, y0, x1, y1)
            text_x = (x0 + x1) / 2
            text_y = (y0 + y1) / 2
            self.coords(self.texts[i], text_x, text_y)
            self.itemconfigure(self.texts[i], text=str(value), fill=self.text_color, font=("Arial", 20))
            self.itemconfigure(self.rectangles[i], fill=self.rectangle_color)

    def animate_sort(self, values, sort_algorithm):
        for swapped in sort_algorithm(values):
            print(swapped)
            self.update_rectangles(values)
            self.update()
            time.sleep(1)

def bubble_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1
        if not swapped:
            break
        yield swapped

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

def heap_sort(arr):
    def head(start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    end = len(arr) - 1
    start = (end - 1) // 2
    for i in range(start, -1, -1):
        head(i, end)
    for i in range(end, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        head(0, i - 1)
        yield arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr

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
            yield arr
            # visualise swap

        arr[low], arr[j] = arr[j], arr[low]
        yield arr
        # visualise swap
        return j

    def sort(arr, low, high):
        if low < high:
            j = yield from partition(arr, low, high)
            yield from sort(arr, low, j - 1)
            yield from sort(arr, j + 1, high)

    length = len(arr)
    sort(arr, 0, length-1)

    yield from sort(arr, 0, len(arr) - 1)

def merge_sort(arr):
    def merge(arr, aux, low, mid, high):
        # left and right arrays are already sorted
        aux = arr.copy()
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                # visualise swap
                arr[k] = aux[j]
                j += 1
            elif j > high:
                # visualise swap
                arr[k] = aux[i]
                i += 1
            elif aux[i] > aux[j]:
                # visualise swap
                arr[k] = aux[j]
                j += 1
            else:
                # visualise swap
                arr[k] = aux[i]
                i += 1
        yield arr

    def sort(arr, aux, low, high):
        if low >= high:
            return
        mid = low + (high - low) // 2
        yield from sort(arr, aux, low, mid)
        yield from sort(arr, aux, mid + 1, high)
        yield from merge(arr, aux, low, mid, high)

    length = len(arr)
    auxArray = [] * (length-1)

    yield from sort(arr, auxArray, 0, length-1)



root = tk.Tk()
canvas = SortingCanvas("#99CC66", "#CCFFFF", root)
canvas.pack(fill = tk.BOTH, expand = True)
values = [5, 2, 8, 1, 3, 7, 9, 6, 10, 4]
canvas.create_rectangles(values)

canvas.animate_sort(values, merge_sort)

