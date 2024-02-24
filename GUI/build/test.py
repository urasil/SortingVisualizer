import tkinter as tk


root = tk.Tk()

elem = 0
score = 0 
answer = 1

sortingType = tk.StringVar()
answer1 = tk.StringVar()
answer2 = tk.StringVar()
answer3 = tk.StringVar()
answer4 = tk.StringVar()
elemLabel = tk.StringVar()
scoreLabel = tk.StringVar()

# FONTS
font = ("Roboto-Light", 25)

# COLOURS
background_col = "#e9e9e9"
button_col = "#d9d9d9"
sorts_col = "#bdd8a6"

# TEMP LABELS
answer1.set("Answer 1")
answer2.set("Answer 2")
answer3.set("Answer 3")
answer4.set("Answer 4")
elemLabel.set("Elements: " + str(elem))
scoreLabel.set("Score: " + str(score))



# SETTING MAIN ROOT
root.geometry('1280x720')
root.title("test")
root["bg"] = background_col


# FUNCTIONS
def back():
    page = pages[0]
    for p in pages:
        p.pack_forget()
    page.pack(pady = 50)


def next():
    for p in pages:
        p.pack_forget()
    pages[1].pack(pady = 10)
    pages[2].pack(pady = 10)
    pages[3].pack(pady = 00)
    pages[4].pack(pady = 5)

def quiz():
    for p in pages:
        p.pack_forget()
    pages[5].pack(pady = 10)
    pages[6].pack(pady = 10)
    pages[7].pack(pady = 50)


def selectionSort():
    global sortingType
    sortingType.set("Selection Sort")
    next()

def insertionSort():
    global sortingType
    sortingType.set("Insertion Sort")
    next()

def mergeSort():
    global sortingType
    sortingType.set("Merge Sort")
    next()

def quickSort():
    global sortingType
    sortingType.set("Quick Sort")
    next()

def heapSort():
    global sortingType
    sortingType.set("Heap Sort")
    next()

def changeScore():
    scoreLabel.set("Score: " + str(score))

def answer1Choice():
    global answer, score
    if answer == 1:
        score += 1
        changeScore()

def answer2Choice():
    global answer, score
    if answer == 2:
        score += 1
        changeScore()

def answer3Choice():
    global answer, score
    if answer == 3:
        score += 1
        changeScore()

def answer4Choice():
    global answer, score
    if answer == 4:
        score += 1
        changeScore()



# TITLE FRAME
title_frame = tk.Frame(root, background=background_col)
title_frame.pack(fill=tk.BOTH)

title = tk.Label(title_frame, text="Sorting Algorithms Visualiser", font = font)
title.pack(side=tk.TOP, pady = 20)


# FRAME INITIALISATION
main_frame = tk.Frame(root, background=background_col)
main_frame.pack(fill=tk.BOTH, expand=  True)

frame_start = tk.Frame(main_frame, background=background_col)
frame_start.pack(side=tk.TOP, pady=50)

frame_sortupper = tk.Frame(main_frame, background=background_col)
frame_sortmiddle = tk.Frame(main_frame, background=background_col)
frame_sortmidlow = tk.Frame(main_frame, background=background_col)
frame_sortlower = tk.Frame(main_frame, background=background_col)

frame_quizupper = tk.Frame(main_frame, background=background_col)
frame_quizmiddle = tk.Frame(main_frame, background=background_col)
frame_quizlower = tk.Frame(main_frame, background=background_col)

# CANVAS INITIALISATION
canvas = tk.Canvas(frame_sortmiddle, bg = "white", width = 1280, height = 350, background = background_col)
canvas.pack(side = tk.TOP)

# Adding the frames to the array
pages = [frame_start, frame_sortupper, frame_sortmiddle, frame_sortmidlow, frame_sortlower, frame_quizupper, frame_quizmiddle, frame_quizlower]


# START FRAME
# ss_image = tk.PhotoImage(file = "/Users/edgar/Desktop/Coding/Engf0002/Scenarios/GUI/build/assets/frame0/button_1.png")
# ss_btn = tk.Button(frame_start, image = ss_image, font = font, command = selectionSort)
ss_btn = tk.Button(frame_start, text = "Selection Sort", font = font, command = selectionSort)
ss_btn.pack(side=tk.TOP, padx=10, pady=10)

# is_image = tk.PhotoImage(file = "/Users/edgar/Desktop/Coding/Engf0002/Scenarios/GUI/build/assets/frame0/button_2.png")
# is_btn = tk.Button(frame_start, image = is_image, font = font, command = insertionSort)
is_btn = tk.Button(frame_start, text = "Insertion Sort", font = font, command = insertionSort)
is_btn.pack(side=tk.TOP, padx=10, pady=10)

# ms_image = tk.PhotoImage(file = "/Users/edgar/Desktop/Coding/Engf0002/Scenarios/GUI/build/assets/frame0/button_3.png")
# ms_btn = tk.Button(frame_start, image = ms_image, font = font, command = mergeSort)
ms_btn = tk.Button(frame_start, text = "Merge Sort", font = font, command = mergeSort)
ms_btn.pack(side=tk.TOP, padx=10, pady=10)

# qs_image = tk.PhotoImage(file = "/Users/edgar/Desktop/Coding/Engf0002/Scenarios/GUI/build/assets/frame0/button_4.png")
# qs_btn = tk.Button(frame_start, image = qs_image, font = font, command = quickSort)
qs_btn = tk.Button(frame_start, text = "Quick Sort", font = font, command = quickSort)
qs_btn.pack(side=tk.TOP, padx=10, pady=10)

# hs_image = tk.PhotoImage(file = "/Users/edgar/Desktop/Coding/Engf0002/Scenarios/GUI/build/assets/frame0/button_5.png")
# hs_btn = tk.Button(frame_start, image = hs_image, font = font, command = heapSort)
hs_btn = tk.Button(frame_start, text = "Heap Sort", font = font, command = heapSort)
hs_btn.pack(side=tk.TOP, padx=10, pady=10)


# SORTING FRAME
sortType = tk.Label(frame_sortupper, textvariable = sortingType, font = font)
sortType.pack(side = tk.TOP, pady = 5, fill = 'y')

elements = tk.Label(frame_sortupper, textvariable = elemLabel, font = font, width=10)
elements.pack(side=tk.TOP,  anchor = 'w')

back_btn = tk.Button(frame_sortmidlow, text = '<', font = font, width=5, bg = button_col)
back_btn.pack(side=tk.LEFT, padx=10, pady=10)

next_btn = tk.Button(frame_sortmidlow, text = '>', font = font, width=5, bg = button_col)
next_btn.pack(side=tk.LEFT, padx=10, pady=10)

moveOn = tk.Label(frame_sortlower, text = "Move on to quiz?", font = font)
moveOn.pack(side=tk.TOP)

no_btn = tk.Button(frame_sortlower, text = 'No', font = font, width=20, command = back, bg = button_col)
no_btn.pack(side=tk.LEFT, padx=10, pady=10)

yes_btn = tk.Button(frame_sortlower, text = 'Yes', font = font, width=20, command = quiz, bg = button_col)
yes_btn.pack(side=tk.LEFT, padx=10, pady=10)


# QUIZ FRAME
sortType = tk.Label(frame_quizupper, textvariable = sortingType, font = font)
sortType.pack(side=tk.LEFT, padx = 100, pady = 10)

# rewatch_image = tk.PhotoImage(file = "/Users/edgar/Desktop/Coding/Engf0002/Scenarios/GUI/build/assets/frame2/button_2.png")
# rewatch_btn = tk.Button(frame_quizupper, image = rewatch_image, font = font, command = next)
rewatch_btn = tk.Button(frame_quizupper, text = "Watch Sorting Process Again", font = font, command = next)
rewatch_btn.pack(side=tk.RIGHT, padx = 100, pady=10)

score_label = tk.Label(frame_quizmiddle, textvariable = scoreLabel, font = font, width=10)
score_label.pack(side=tk.TOP,  anchor = 'w')

question = tk.Label(frame_quizlower, text = "Example Question", font = font)
question.pack(side=tk.TOP, pady = 25)

ans1_btn = tk.Button(frame_quizlower, textvariable = answer1, font = font, width=10, bg = button_col, command = answer1Choice)
ans1_btn.pack(side=tk.LEFT, padx=10, pady=10)

ans2_btn = tk.Button(frame_quizlower, textvariable = answer2, font = font, width=10, bg = button_col, command = answer2Choice)
ans2_btn.pack(side=tk.LEFT, padx=10, pady=10)

ans3_btn = tk.Button(frame_quizlower, textvariable = answer3, font = font, width=10, bg = button_col, command = answer3Choice)
ans3_btn.pack(side=tk.LEFT, padx=10, pady=10)

ans4_btn = tk.Button(frame_quizlower, textvariable = answer4, font = font, width=10, bg = button_col, command = answer4Choice)
ans4_btn.pack(side=tk.LEFT, padx=10, pady=10)




# BOTTOM FRAME FOR TESTING
# bottom_frame = tk.Frame(root)

# Back_btn = tk.Button(bottom_frame, text = 'Back', font = font, width=20, command = back)
# Back_btn.pack(side=tk.LEFT, padx=10, pady=10)

# Next_btn = tk.Button(bottom_frame, text = 'Next', font = font, width=20, command = next)
# Next_btn.pack(side=tk.RIGHT, padx=10, pady=10)

# bottom_frame.pack(side=tk.BOTTOM, pady = 25)


# MAIN LOOP
root.mainloop()