import tkinter as tk
import time
import random

from tkinter import *

class SortingCanvas(Canvas):
    def __init__(self, rectangle_color, text_color, parent, width=800, height=600):
        super().__init__(parent, width=width, height=height)
        self.rectangle_color = rectangle_color
        self.text_color = text_color
        self.parent = parent
        self.width = width
        self.height = height
        self.steps = []
        self.current_step = 0
        self.step_label = Label(self.parent, text="Sorting Step: 0/0", font=("Arial", 20))
        self.step_label.pack(side=TOP, pady=10)
        self.pack(side=RIGHT)

    def animate_sort(self, sort_func, array):
        self.steps = sort_func(array)
        print(self.steps, len(self.steps))
        self.step_label.config(text=f"Sorting Step: {self.current_step + 1}/{len(self.steps)}")
        self.create_rectangles(self.steps[self.current_step])

    def create_rectangles(self, data):
        self.delete("all")
        bar_width = self.width // len(data)
        for i, height in enumerate(data):
            x0 = i * bar_width
            y0 = self.height
            x1 = (i + 1) * bar_width
            y1 = self.height - height * self.height / max(data)
            # color = '#' + format(0x1000000 + 0xFFFFFF * i // len(data), '06x')
            self.create_rectangle(x0, y0, x1, y1, fill=self.rectangle_color)
            self.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(height), font=("Arial", 10), fill=self.text_color)

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.create_rectangles(self.steps[self.current_step])
            self.step_label.config(text=f"Sorting Step: {self.current_step + 1}/{len(self.steps)}")

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.create_rectangles(self.steps[self.current_step])
            self.step_label.config(text=f"Sorting Step: {self.current_step + 1}/{len(self.steps)}")





class SortingCanvas2(tk.Canvas):
    def __init__(self, rectangle_color, text_color, valuelist, master, **kwargs):
        super().__init__(master, **kwargs)
        self.rectangles = []
        self.texts = []
        self.rectangle_color = rectangle_color
        self.text_color = text_color
        # self.algorithm = algorithm
        # self.valuelist = self.algorithm(valuelist)
        self.valuelist = valuelist
        print(self.valuelist)
        self.sortindex = 0

        # create control buttons
        self.next_button = Button(master, text="Next Step", command=self.next_step)
        self.next_button.pack(side=LEFT)
        self.prev_button = Button(master, text="Prev Step", command=self.prev_step)
        self.prev_button.pack(side=LEFT)

    def next_step(self):
        self.sortindex += 1
        self.update_rectangles(self.valuelist[self.sortindex])

    def prev_step(self):
        self.sortindex -= 1
        self.update_rectangles(self.valuelist[self.sortindex])

    def create_rectangles(self, values):
        # self.delete("all")
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
        # time.sleep(2)

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
        # self.update()
        # time.sleep(2)

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

def insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
        yield values

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
                root = child
            else:
                break

    end = len(values) - 1
    start = (end - 1) // 2
    for i in range(start, -1, -1):
        sift_down(i, end)
    for i in range(end, 0, -1):
        values[i], values[0] = values[0], values[i]
        sift_down(0, i - 1)
        yield values

def selection_sort(values):
    for i in range(len(values)):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
        yield values

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


def bubble_sort2(values):
    n = len(values)
    arrs = [values.copy()]

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
                arrs.append(values.copy())
        if not swapped:
            break
    return arrs

values = [5, 3, 8, 6, 7, 2, 4, 1]
root = tk.Tk()
canvas = SortingCanvas2("#99CC66", "#CCFFFF", bubble_sort2(values), root)
canvas.pack(fill = tk.BOTH, expand = True)
canvas.create_rectangles(values)

canvas.update_rectangles(values)

canvas.animate_sort(values, merge_sort)




# Create a tkinter window
root = tk.Tk()
# Create a SortingCanvas instance with a list of values and the parent window
values = [4, 7, 1, 3, 8, 5, 9, 2, 10, 6]
canvas = SortingCanvas("#99CC66", "#CCFFFF", root)
# Call the animate_sort method with the bubble_sort algorithm function
canvas.animate_sort(bubble_sort2, values)
# Run the tkinter main loop
root.mainloop()