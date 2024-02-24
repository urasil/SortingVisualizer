from tkinter import *
from SortingAlgorithm import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort

window = Tk()
rectangles = []
texts = []
WIDTH = 600
HEIGHT = 400
VALUES = [10, 3, 1, 9, 8, 6, 7, 2, 4, 5]
RECCOLOR = "#99CC66"
HIGHLIGHTCOLOR = "#FFCC33"
TEXTCOLOR = "#CCFFFF"
SORTINDEX = 0
Sorts = {"bubble_sort": 0, "selection_sort": 1, "insertion_sort": 2, "merge_sort": 3, "quick_sort": 4, "heap_sort": 5}
AlgorithmName = "heap_sort"
valuelist, highlightIndexs = heap_sort(VALUES.copy())

def next_step():
    global SORTINDEX, valuelist
    if 0 <= SORTINDEX+1 <= len(valuelist)-1:
        SORTINDEX += 1
        update_rectangles(valuelist[SORTINDEX], highlightIndexs[SORTINDEX])
        canvas.step_label.config(text=f"Sorting Step: {SORTINDEX + 1}/{len(valuelist)}")
        canvas.update()

def prev_step():
    global SORTINDEX, valuelist
    if 0 <= SORTINDEX-1 <= len(valuelist)-1:
        SORTINDEX -= 1
        update_rectangles(valuelist[SORTINDEX], highlightIndexs[SORTINDEX])
        canvas.step_label.config(text=f"Sorting Step: {SORTINDEX + 1}/{len(valuelist)}")
        canvas.update()

def update_rectangles(values, highlights):
    global WIDTH, HEIGHT
    print(values)
    bar_width = WIDTH / len(values)
    for i, value in enumerate(values):
        x0 = i * bar_width
        y0 = HEIGHT
        x1 = (i + 1) * bar_width
        y1 = HEIGHT - (value / max(values)) * HEIGHT
        canvas.coords(rectangles[i], x0, y0, x1, y1)
        text_x = (x0 + x1) / 2
        text_y = (y0 + y1) / 2
        canvas.coords(texts[i], text_x, text_y)
        canvas.itemconfigure(texts[i], text=str(value), fill=TEXTCOLOR, font=("Arial", 20))
        if i in highlights:
            canvas.itemconfigure(rectangles[i], fill=HIGHLIGHTCOLOR)
        else:
            canvas.itemconfigure(rectangles[i], fill=RECCOLOR)

# Animation Canvas
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
window.geometry("1163x660")
canvas.place(x=0, y=0)

# Step label
canvas.step_label = Label(window, text="Sorting Step: 0/0", font=("Arial", 20))
canvas.step_label.pack(side=TOP, pady=10)
canvas.pack(side=RIGHT)
canvas.step_label.config(text=f"Sorting Step: 0/{len(valuelist)}")

# create control buttons
next_button = Button(window, text="Next Step", command=next_step)
next_button.pack(side=RIGHT)
prev_button = Button(window, text="Prev Step", command=prev_step)
prev_button.pack(side=RIGHT)

# Initialise the rectangles
bar_width = WIDTH / len(VALUES)
for i, value in enumerate(VALUES):
    x0 = i * bar_width
    y0 = HEIGHT
    x1 = (i + 1) * bar_width
    y1 = HEIGHT - (value / max(VALUES)) * HEIGHT
    rectangle = canvas.create_rectangle(x0, y0, x1, y1, fill=RECCOLOR)
    rectangles.append(rectangle)
    text_x = (x0 + x1) / 2
    text_y = (y0 + y1) / 2
    text = canvas.create_text(text_x, text_y, text=str(value), fill=TEXTCOLOR, font=("Arial", 20))
    texts.append(text)


# Algorithm Descriptions
DescripDict = {}
with open ("AlgsDescrip.txt") as f:
    currentAlgs = ""
    currentDescrip = ""
    for line in f:
        if ":::" in line:
            currentAlgs = line.strip().replace(":", "")
            DescripDict[currentAlgs] = ""
        elif line.strip() != "":
            currentDescrip += line.strip()
        else:
            DescripDict[currentAlgs] = currentDescrip.strip()
            currentDescrip = ""


lines = DescripDict[AlgorithmName].split(".")
lines = [elem + ".\n" for elem in lines][:-1]
# , state="disabled"
text_widget = Text(window, width=100, height=30, wrap="word", background="#FFFFCC")
text_widget.pack(side=LEFT)
text_widget.tag_config("beauty", font=("Helvetica", 16), foreground="#0099CC")
for line in lines:
    text_widget.insert(END, line, "beauty")


# Show Hints
HintsDict = {}
with open ("AlgsExplain.txt") as f2:
    currentAlgs = ""
    currentHint = ""
    for line in f2:
        if ":::" in line:
            currentAlgs = line.strip().replace(":", "")
            HintsDict[currentAlgs] = ""
        else:
            HintsDict[currentAlgs] += line.replace("\n", "")

hint_lines = HintsDict[AlgorithmName].split(".")
hint_lines = [elem + ".\n" for elem in hint_lines][:-1]

def show_hints():
    hints_window = Toplevel(window)
    hints_window.title("Hints")
    hints_window.geometry("600x400+100+100")
    hints_window.transient(window)
    hints_window.grab_set()

    hints_text = Text(hints_window, width=150, height=50)
    hints_text.tag_config("beauty", font=("Arial", 16), foreground="black")
    hints_text.pack()

    for hint in hint_lines:
        hints_text.insert(END, hint + "\n")

    cancel_button = Button(hints_window, text="Cancel", command=hints_window.destroy)
    cancel_button.pack()

hints_button = Button(window, text="Show Hints", command=show_hints)
hints_button.place(x=435,  y=500)
hints_button.configure(font=("Arial", 14), bg="lightblue")


window.mainloop()
