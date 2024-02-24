import tkinter as tk
import random
from SortingAlgorithm import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
from quizEditor import *


root = tk.Tk()

elem = 10
score = 0
answer = 1

sortingType = tk.StringVar()
txt_files = []   #the list of all available quiz files
quizLibPath = "./quizLibrary"
questionContent = tk.StringVar()
answer1 = tk.StringVar()
answer2 = tk.StringVar()
answer3 = tk.StringVar()
answer4 = tk.StringVar()
explanation = tk.StringVar()
elemLabel = tk.StringVar()
scoreLabel = tk.StringVar()
#explanationLabel = tk.StringVar()
description = tk.StringVar()

# For Animation
ANIMATIONCANVASWIDTH = 1280 / 2
ANIMATIONCANVASHEIGHT = 400
rectangles = []
texts = []
VALUES = [10, 3, 1, 9, 8, 6, 7, 2, 4, 5]
RECCOLOR = "#99CC66"
HIGHLIGHTCOLOR = "#FFCC33"
TEXTCOLOR = "#CCFFFF"
SORTINDEX = 0
AlgorithmName = ""
valuelist = [[]]
highlightIndexs = []

# FONTS

font = ("Roboto-Light", int((25/1000)*(root.winfo_screenheight() - root.winfo_toplevel().winfo_height())))
font2 = ("Roboto-Light", int((25/1000)*(root.winfo_screenheight() - root.winfo_toplevel().winfo_height())))
font3 = ("Roboto-Light", int((18/1000)*(root.winfo_screenheight() - root.winfo_toplevel().winfo_height())))
explanationFont = ("Roboto-Light",12)
answerFont = ("Roboto-Light",16)
questionFont = ("Roboto-Light",20)

# COLOURS
background_col = "#ececec"
button_col = "#d9d9d9"
sorts_col = "#bdd8a6"

# TEMP LABELS
questionContent.set("Example question")
answer1.set("Answer 1")
answer2.set("Answer 2")
answer3.set("Answer 3")
answer4.set("Answer 4")
explanation.set("Explanation")
elemLabel.set("Elements: " + str(elem))
scoreLabel.set("Score: " + str(score))


# SETTING MAIN ROOT
# root.geometry('1280x1020')
taskbar_height = root.winfo_screenheight() - root.winfo_toplevel().winfo_height()
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), taskbar_height))
root.title("test")
root["bg"] = background_col

# FUNCTIONS
def back():
    for p in pages:
        p.pack_forget()
    pages[0].pack(pady = 50)


def next():
    for p in pages:
        p.pack_forget()
    pages[1].pack(pady = 10)
    pages[2].pack(pady = 10)
    pages[3].pack(pady = 10)
    pages[5].pack(pady = 00)

def quiz():
    for p in pages:
        p.pack_forget()
    readQuizList()
    setQuiz()
    pages[6].pack(pady = 10)
    pages[7].pack(pady = 10)
    pages[8].pack(pady = 20)
    pages[9].pack(pady = 10)
    #explanationLabel.pack(side=tk.TOP)

def bubbleSort():
    global sortingType, valuelist, highlightIndexs, AlgorithmName
    sortingType.set("Bubble Sort")
    valuelist, highlightIndexs = bubble_sort(VALUES.copy())
    AlgorithmName = "bubble_sort"
    AnimationCanvas()
    next()

def selectionSort():
    global sortingType, valuelist, highlightIndexs, AlgorithmName
    sortingType.set("Selection Sort")
    valuelist, highlightIndexs = selection_sort(VALUES.copy())
    AlgorithmName = "selection_sort"
    AnimationCanvas()
    next()

def insertionSort():
    global sortingType, valuelist, highlightIndexs, AlgorithmName
    sortingType.set("Insertion Sort")
    valuelist, highlightIndexs = insertion_sort(VALUES.copy())
    AlgorithmName = "insertion_sort"
    AnimationCanvas()
    next()

def mergeSort():
    global sortingType, valuelist, highlightIndexs, AlgorithmName
    sortingType.set("Merge Sort")
    valuelist, highlightIndexs = merge_sort(VALUES.copy())
    AlgorithmName = "merge_sort"
    AnimationCanvas()
    next()

def quickSort():
    global sortingType, valuelist, highlightIndexs, AlgorithmName
    sortingType.set("Quick Sort")
    valuelist, highlightIndexs = quick_sort(VALUES.copy())
    AlgorithmName = "quick_sort"
    AnimationCanvas()
    next()

def heapSort():
    global sortingType, valuelist, highlightIndexs, AlgorithmName
    sortingType.set("Heap Sort")
    valuelist, highlightIndexs = heap_sort(VALUES.copy())
    AlgorithmName = "heap_sort"
    AnimationCanvas()
    next()

def changeScore():
    scoreLabel.set("Score: " + str(score))

def answer1Choice():
    global answer, score ,explanationLabel
    if answer == 1:
        score += 1
        changeScore()
        #explanationLabel.pack_forget()   #when correct answer, hide the explanation for the next question
        setQuiz()
        questionOver()
    else:

        explanationLabel.pack(side=tk.LEFT)
        


def answer2Choice():
    global answer, score,explanationLabel
    if answer == 2:
        score += 1
        changeScore()
        # explanationLabel.pack_forget()   #when correct answer, hide the explanation for the next question
        setQuiz()
        questionOver()
    else:
        explanationLabel.pack(side=tk.TOP)


def answer3Choice():
    global answer, score,explanationLabel
    if answer == 3:
        score += 1
        changeScore()
        # explanationLabel.pack_forget()   #when correct answer, hide the explanation for the next question
        setQuiz()
        questionOver()
    else:
        explanationLabel.pack(side=tk.TOP)


def answer4Choice():
    global answer, score,explanationLabel
    if answer == 4:
        score += 1
        changeScore()
        # explanationLabel.pack_forget()     #when correct answer, hide the explanation for the next question
        setQuiz()
        questionOver()
    else:
        explanationLabel.pack(side=tk.TOP)

        

def questionOver():
    global explanationLabel,backToMainLabel
    if questionContent.get() == "No more question":
        explanationLabel.pack_forget()
        backToMainLabel.pack(side=tk.TOP)
    else:
        #explanationLabel.pack_forget()
        backToMainLabel.pack_forget()

def readQuizList():
    global txt_files
    availableFiles = os.listdir(quizLibPath)
    txt_files = [f for f in availableFiles if f.endswith('.txt')]  #make sure only txt file is accepted
    
def setQuiz():
    global answer,questionContent,answer1,answer2,answer3,answer4,explanation,txt_files
    
    if len(txt_files) == 0: # if file exists, then continue to read
        questionContent.set("No more question")
        answer1.set("N/A")
        answer2.set("N/A")
        answer3.set("N/A")
        answer4.set("N/A")
        explanation.set("N/A")
        answer = 0   # No correct answer

        #return True

    else:    
        explanationLabel.pack_forget()
        randomFile = random.choice(txt_files)    
        txt_files.remove(randomFile)   #avoid repeating the same question
        randomFilePath = os.path.join(quizLibPath,randomFile)
        newQuiz = Quiz()
        newQuiz.quizRead(randomFilePath)
        __question, __imageLink, __choices, __answer,__explanation = newQuiz.getQuiz()   #here image link is not used temporarilly
        questionContent.set(__question)
        answer = int(__answer)
        explanation.set(__explanation)
        if len(__choices) == 4:
            answer1.set(__choices[0])
            answer2.set(__choices[1])
            answer3.set(__choices[2])
            answer4.set(__choices[3])
        elif len(__choices) == 3:
            answer1.set(__choices[0])
            answer2.set(__choices[1])
            answer3.set(__choices[2])
            answer4.set("N/A")
        elif len(__choices) == 2:
            answer1.set(__choices[0])
            answer2.set(__choices[1])
            answer3.set("N/A")
            answer4.set("N/A")

        #return False

        

def openEditor():

    newWindow = tk.Toplevel(root)
    newWindow.title("Editor")
 
    # sets the geometry of toplevel
    newWindow.geometry("1280x720")
    frame1 = QuizEditorFrame(newWindow)
    frame1.pack()

# TITLE FRAME
title_frame = tk.Frame(root, background=background_col)
title_frame.pack(fill=tk.BOTH)

title = tk.Label(title_frame, text="Sorting Algorithms Visualiser", font = font)
title.pack(side=tk.TOP, pady = 20)


# FRAME INITIALISATION
main_frame = tk.Frame(root, background=background_col)
main_frame.pack(fill=tk.BOTH, expand= True)

frame_start = tk.Frame(main_frame, background=background_col)
frame_start.pack(side=tk.TOP, pady=50)

frame_sortupper = tk.Frame(main_frame, background=background_col)
frame_sortmiddle = tk.Frame(main_frame, background=background_col)
frame_sortmidlow = tk.Frame(main_frame, background=background_col)
frame_sortlower = tk.Frame(main_frame, background=background_col)
frame_sortlowest = tk.Frame(main_frame, background=background_col)

frame_quizupper = tk.Frame(main_frame, background=background_col)
frame_quizmiddle = tk.Frame(main_frame, background=background_col)
frame_quizlower = tk.Frame(main_frame, background=background_col)
frame_quizlowest = tk.Frame(main_frame, background=background_col)

frame_compare = tk.Frame(main_frame, background=background_col)

# CANVAS INITIALISATION
canvas = tk.Canvas(frame_sortmiddle, bg = "white", width = ANIMATIONCANVASWIDTH, height = ANIMATIONCANVASHEIGHT, background = background_col, highlightthickness=0)
canvas.pack(side = tk.TOP)

# Adding the frames to the array
pages = [frame_start, frame_sortupper, frame_sortmiddle, frame_sortmidlow, frame_sortlower, frame_sortlowest, frame_quizupper, frame_quizmiddle, frame_quizlower, frame_quizlowest, frame_compare]


# START FRAME
bs_btn = tk.Button(frame_start, text = "Bubble Sort", font = font, command = bubbleSort)
bs_btn.pack(side=tk.TOP, padx=10, pady=10)

ss_btn = tk.Button(frame_start, text = "Selection Sort", font = font, command = selectionSort)
ss_btn.pack(side=tk.TOP, padx=10, pady=10)

is_btn = tk.Button(frame_start, text = "Insertion Sort", font = font, command = insertionSort)
is_btn.pack(side=tk.TOP, padx=10, pady=10)

ms_btn = tk.Button(frame_start, text = "Merge Sort", font = font, command = mergeSort)
ms_btn.pack(side=tk.TOP, padx=10, pady=10)

qs_btn = tk.Button(frame_start, text = "Quick Sort", font = font, command = quickSort)
qs_btn.pack(side=tk.TOP, padx=10, pady=10)

hs_btn = tk.Button(frame_start, text = "Heap Sort", font = font, command = heapSort)
hs_btn.pack(side=tk.TOP, padx=10, pady=10)

editor_btn = tk.Button(frame_start, text = "Quiz Question Editor", font = font, command = openEditor)
editor_btn.pack(side=tk.TOP, padx=10, pady=10)



# SORTING FRAME
def AnimationCanvas():
    while SORTINDEX > 0:
        prev_step()
    RemoveRectangles(canvas)
    RemoveRectangles(canvas_compare1)
    RemoveRectangles(canvas_compare2)
    rectangles.clear()
    texts.clear()
    InitRectangles()
    readDescripFile()


def next_step():
    global SORTINDEX, valuelist
    if 0 <= SORTINDEX+1 <= len(valuelist)-1:
        SORTINDEX += 1
        update_rectangles(valuelist[SORTINDEX], highlightIndexs[SORTINDEX])
        canvas.step_label.config(text=f"Sorting Step: {SORTINDEX + 1}/{len(valuelist)}")
        canvas.update()
    if SORTINDEX == len(valuelist)-1:
        print("finish")
        frame_sortmiddle.pack_forget()
        frame_sortmidlow.pack_forget()
        frame_sortlowest.pack_forget()
        frame_sortlower.pack(side = tk.TOP, pady=60)


def prev_step():
    global SORTINDEX, valuelist
    if 0 <= SORTINDEX-1 <= len(valuelist)-1:
        SORTINDEX -= 1
        update_rectangles(valuelist[SORTINDEX], highlightIndexs[SORTINDEX])
        canvas.step_label.config(text=f"Sorting Step: {SORTINDEX + 1}/{len(valuelist)}")
        canvas.update()


def update_rectangles(values, highlights):
    global ANIMATIONCANVASWIDTH, ANIMATIONCANVASHEIGHT
    print(values)
    bar_width = ANIMATIONCANVASWIDTH / len(values)
    for i, value in enumerate(values):
        x0 = i * bar_width
        y0 = ANIMATIONCANVASHEIGHT
        x1 = (i + 1) * bar_width
        y1 = ANIMATIONCANVASHEIGHT - (value / max(values)) * ANIMATIONCANVASHEIGHT
        canvas.coords(rectangles[i], x0, y0, x1, y1)
        text_x = (x0 + x1) / 2
        text_y = (y0 + y1) / 2
        canvas.coords(texts[i], text_x, text_y)
        canvas.itemconfigure(texts[i], text=str(value), fill=TEXTCOLOR, font=font2)
        if i in highlights:
            canvas.itemconfigure(rectangles[i], fill=HIGHLIGHTCOLOR)
        else:
            canvas.itemconfigure(rectangles[i], fill=RECCOLOR)

# Step label
canvas.step_label = tk.Label(frame_sortupper, text="Sorting Step: 0/0", font=font2)
canvas.step_label.pack(side=tk.TOP, pady=10)
canvas.pack(side=tk.RIGHT)
canvas.step_label.config(text=f"Sorting Step: 0/{len(valuelist)}")


# Initialise the rectangles
def InitRectangles():
    bar_width = ANIMATIONCANVASWIDTH / len(VALUES)
    for i, value in enumerate(VALUES):
        x0 = i * bar_width
        y0 = ANIMATIONCANVASHEIGHT
        x1 = (i + 1) * bar_width
        y1 = ANIMATIONCANVASHEIGHT - (value / max(VALUES)) * ANIMATIONCANVASHEIGHT
        rectangle = canvas.create_rectangle(x0, y0, x1, y1, fill=RECCOLOR)
        rectangles.append(rectangle)
        text_x = (x0 + x1) / 2
        text_y = (y0 + y1) / 2
        text = canvas.create_text(text_x, text_y, text=str(value), fill=TEXTCOLOR, font=font2)
        texts.append(text)

def RemoveRectangles(canvas):
    for i in rectangles:
        canvas.delete(i)
    for i in texts:
        canvas.delete(i)


# Algorithm Descriptions
def readDescripFile():
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
    lines = [elem + ".\n\n" for elem in lines][:-1]

    text_widget.pack(side=tk.LEFT, padx = 10)
    descStr = ""
    for line in lines:
        descStr += line
    description.set(descStr)


# Show Hints
def readExplainFile():
    HintsDict = {}
    with open ("AlgsExplain.txt") as f2:
        currentHint = ""
        for line in f2:
            if ":::" in line:
                currentHint = line.strip().replace(":", "")
                HintsDict[currentHint] = ""
            else:
                HintsDict[currentHint] += line.replace("\n", "")

    hint_lines = HintsDict[AlgorithmName].split(".")
    hint_lines = [elem + ".\n" for elem in hint_lines][:-1]
    return hint_lines

def show_hints():
    hints_window = tk.Toplevel(root)
    hints_window.title("Hints")
    hints_window.geometry("600x400+400+200")
    hints_window.transient(root)
    hints_window.grab_set()

    hints_text = tk.Text(hints_window, width=250, height=50)
    hints_text.tag_config("beautyHint", font=font2, foreground="black")
    hints_text.pack()

    hint_lines = readExplainFile()
    for hint in hint_lines:
        hints_text.insert(tk.END, hint, "beautyHint")

    hints_text.config(state="disabled")

    cancel_button = tk.Button(hints_window, text="Cancel", command=hints_window.destroy)
    cancel_button.pack()

text_widget = tk.Label(frame_sortmiddle, wraplength = 500, textvariable=description, background=background_col, highlightthickness=0, font = ("Roboto-Light", 14))

hints_button = tk.Button(frame_sortmidlow, text="Show Hints",font = font, width=10, bg = button_col, command=show_hints)
hints_button.pack(side=tk.RIGHT, padx=10)


# Other Elements
sortType = tk.Label(frame_sortupper, textvariable = sortingType, font = font)
sortType.pack(side = tk.TOP, pady = 5, fill = 'y')

back_btn = tk.Button(frame_sortmidlow, text = 'Prev Step', font = font, width=10, bg = button_col, command=prev_step)
back_btn.pack(side=tk.LEFT, padx=10, pady=10)

next_btn = tk.Button(frame_sortmidlow, text = 'Next Step', font = font, width=10, bg = button_col, command=next_step)
next_btn.pack(side=tk.LEFT, padx=10, pady=10)

moveOn = tk.Label(frame_sortlower, text = "Move on to quiz?", font = font)
moveOn.pack(side=tk.TOP)

no_btn = tk.Button(frame_sortlower, text = 'No', font = font, width=20, command = next, bg = button_col)
no_btn.pack(side=tk.LEFT, padx=10, pady=10)

yes_btn = tk.Button(frame_sortlower, text = 'Yes', font = font, width=20, command = quiz, bg = button_col)
yes_btn.pack(side=tk.LEFT, padx=10, pady=10)

main_btn = tk.Button(frame_sortlowest, text = 'Back', font = font, width=10, bg = button_col, command=back)
main_btn.pack(side=tk.LEFT, padx=10, pady=10)


# QUIZ FRAME
sortType = tk.Label(frame_quizupper, textvariable = sortingType, font = font)
sortType.pack(side=tk.LEFT, padx = 100, pady = 10)

rewatch_btn = tk.Button(frame_quizupper, text = "Watch Sorting Process Again", font = font, command = next)
rewatch_btn.pack(side=tk.RIGHT, padx = 100, pady=10)

score_label = tk.Label(frame_quizmiddle, textvariable = scoreLabel, font = font, width=10)
score_label.pack(side=tk.TOP,  anchor = 'w')

question = tk.Label(frame_quizlower, textvariable=questionContent, font = questionFont)
question.pack(side=tk.TOP, pady = 25)

ans1_btn = tk.Button(frame_quizlower, textvariable = answer1, font = answerFont, width=15, bg = button_col, command = answer1Choice)
ans1_btn.pack(side=tk.LEFT, padx=10, pady=10)

ans2_btn = tk.Button(frame_quizlower, textvariable = answer2, font = answerFont, width=15, bg = button_col, command = answer2Choice)
ans2_btn.pack(side=tk.LEFT, padx=10, pady=10)

ans3_btn = tk.Button(frame_quizlower, textvariable = answer3, font = answerFont, width=15, bg = button_col, command = answer3Choice)
ans3_btn.pack(side=tk.LEFT, padx=10, pady=10)

ans4_btn = tk.Button(frame_quizlower, textvariable = answer4, font = answerFont, width=15, bg = button_col, command = answer4Choice)
ans4_btn.pack(side=tk.LEFT, padx=10, pady=10)


explanationLabel = tk.Label(frame_quizlowest, textvariable=explanation, font=explanationFont)
# explanationLabel.pack(side=tk.LEFT)

backToMainLabel = tk.Button(frame_quizlowest,text="Main Menu",font=font, bg=button_col, command=back)
# backToMainLabel.pack(side=tk.TOP)




# Compare 2 Algorithms
def copmareAlgos():
    frame_start.pack_forget()
    frame_compare.pack(pady=10)
    AnimationCompareCanvas()


compare_first_frame = tk.Frame(frame_compare, background=background_col, height=200, width=root.winfo_screenwidth()*0.95)
compare_first_frame.pack(side=tk.TOP)
compare_first_frame.pack_propagate(0)

# Create 2 selectors to choose different algorithms
label1 = tk.Label(compare_first_frame, text="Select compared algorithm", font = font3)
label1.grid(row=0, column=0, padx=10, pady=10)
selector1 = tk.Listbox(compare_first_frame, height=6 , font=font3)
selector1.grid(row=1, column=0, padx=10, pady=10)
sortslist = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]
for item in sortslist:
    selector1.insert(tk.END, item)

label2 = tk.Label(compare_first_frame, text="Select algorithm to compare:", font = font3)
label2.grid(row=0, column=50, padx=10, pady=10)
selector2 = tk.Listbox(compare_first_frame, height=6, font=font3)
selector2.grid(row=1, column=50, padx=10, pady=10)
for item in sortslist:
    selector2.insert(tk.END, item)

selectedItem1 = ""
selectedItem2 = ""

select_button1 = tk.Label(compare_first_frame, text="First Algorithm", font=font2)
select_button1.grid(row=1, column=10, padx=10, pady=10)
select_button2 = tk.Label(compare_first_frame, text="Second Algorithm", font=font2)
select_button2.grid(row=1, column=30, padx=10, pady=10)

def select1():
    global selectedItem1
    selected = selector1.get(selector1.curselection())
    selectedItem1 = selected
    select_button1.configure(text=selected)


def select2():
    global selectedItem1, selectedItem2
    selected = selector2.get(selector2.curselection())
    if selectedItem1 == selected:
        select_button2.configure(text="Please choose a different algorithm!")
    else:
        select_button2.configure(text=selected)
        selectedItem2 = selected


button1 = tk.Button(compare_first_frame, text="Select", font=font, command=select1)
button1.grid(row=0, column=2, padx=10, pady=10)

button2 = tk.Button(compare_first_frame, text="Select", font=font, command=select2)
button2.grid(row=0, column=48, padx=10, pady=10)


# Get the animation algorithms
COMPAREINDEX1 = 0
COMPAREINDEX2 = 0
COMPARELIST1 = [[]]
COMPAREINDEXES1 = [[]]
COMPARELIST2 = [[]]
COMPAREINDEXES2 = [[]]

def AnimationCompareCanvas():
    while COMPAREINDEX1 > 0:
        prevStep1()
    while COMPAREINDEX2 > 0:
        prevStep2()
    RemoveRectangles(canvas)
    RemoveRectangles(canvas_compare1)
    RemoveRectangles(canvas_compare2)
    rectangles.clear()
    texts.clear()
    InitRecs(canvas_compare1)
    InitRecs(canvas_compare2)


def nextStep1():
    global COMPAREINDEX1, COMPARELIST1
    if 0 <= COMPAREINDEX1 + 1 <= len(COMPARELIST1) - 1:
        COMPAREINDEX1 += 1
        updateRectangles(canvas_compare1, COMPARELIST1[COMPAREINDEX1], COMPAREINDEXES1[COMPAREINDEX1])
        canvas_compare1.update()


def prevStep1():
    global COMPAREINDEX1, COMPARELIST1
    if 0 <= COMPAREINDEX1 - 1 <= len(COMPARELIST1) - 1:
        COMPAREINDEX1 -= 1
        updateRectangles(canvas_compare1, COMPARELIST1[COMPAREINDEX1], COMPAREINDEXES1[COMPAREINDEX1])
        canvas_compare1.update()

def nextStep2():
    global COMPAREINDEX2, COMPARELIST2
    if 0 <= COMPAREINDEX2 + 1 <= len(COMPARELIST2) - 1:
        COMPAREINDEX2 += 1
        updateRectangles(canvas_compare2, COMPARELIST2[COMPAREINDEX2], COMPAREINDEXES2[COMPAREINDEX2])
        canvas_compare2.update()

def prevStep2():
    global COMPAREINDEX2, COMPARELIST2
    if 0 <= COMPAREINDEX2 - 1 <= len(COMPARELIST2) - 1:
        COMPAREINDEX2 -= 1
        updateRectangles(canvas_compare2, COMPARELIST2[COMPAREINDEX2], COMPAREINDEXES2[COMPAREINDEX2])
        canvas_compare2.update()


def updateRectangles(canvas, values, highlights):
    global ANIMATIONCANVASWIDTH, ANIMATIONCANVASHEIGHT
    print(values)
    bar_width = ANIMATIONCANVASWIDTH / len(values)
    for i, value in enumerate(values):
        x0 = i * bar_width
        y0 = ANIMATIONCANVASHEIGHT
        x1 = (i + 1) * bar_width
        y1 = ANIMATIONCANVASHEIGHT - (value / max(values)) * ANIMATIONCANVASHEIGHT
        canvas.coords(rectangles[i], x0, y0, x1, y1)
        text_x = (x0 + x1) / 2
        text_y = (y0 + y1) / 2
        canvas.coords(texts[i], text_x, text_y)
        canvas.itemconfigure(texts[i], text=str(value), fill=TEXTCOLOR, font=font2)
        if i in highlights:
            canvas.itemconfigure(rectangles[i], fill=HIGHLIGHTCOLOR)
        else:
            canvas.itemconfigure(rectangles[i], fill=RECCOLOR)


# Initialise the rectangles
def InitRecs(canvas):
    bar_width = ANIMATIONCANVASWIDTH / len(VALUES)
    for i, value in enumerate(VALUES):
        x0 = i * bar_width
        y0 = ANIMATIONCANVASHEIGHT
        x1 = (i + 1) * bar_width
        y1 = ANIMATIONCANVASHEIGHT - (value / max(VALUES)) * ANIMATIONCANVASHEIGHT
        rectangle = canvas.create_rectangle(x0, y0, x1, y1, fill=RECCOLOR)
        rectangles.append(rectangle)
        text_x = (x0 + x1) / 2
        text_y = (y0 + y1) / 2
        text = canvas.create_text(text_x, text_y, text=str(value), fill=TEXTCOLOR, font=font2)
        texts.append(text)


def chooseCompare(algorithmName):
    lists, indexes = [[]], [[]]
    if algorithmName == sortslist[0]:
        lists, indexes = bubble_sort(VALUES.copy())
    elif algorithmName == sortslist[1]:
        lists, indexes = selection_sort(VALUES.copy())
    elif algorithmName == sortslist[2]:
        lists, indexes = insertion_sort(VALUES.copy())
    elif algorithmName == sortslist[3]:
        lists, indexes = merge_sort(VALUES.copy())
    elif algorithmName == sortslist[4]:
        lists, indexes = quick_sort(VALUES.copy())
    elif algorithmName == sortslist[5]:
        lists, indexes = heap_sort(VALUES.copy())
    return lists, indexes


def showAnimationCompare():
    global selectedItem1, selectedItem2, COMPARELIST1, COMPAREINDEXES1, COMPARELIST2, COMPAREINDEXES2, COMPAREINDEX1, COMPAREINDEX2
    COMPAREINDEX1, COMPAREINDEX2 = 0, 0

    if selectedItem1 != "" and selectedItem2 != "" and selectedItem1 != selectedItem2:
        COMPARELIST1, COMPAREINDEXES1 = chooseCompare(selectedItem1)
        COMPARELIST2, COMPAREINDEXES2 = chooseCompare(selectedItem2)


# Animation Canvas
canvas_compare1 = tk.Canvas(frame_compare, bg = "white", width = 1280/2, height = 400, background = background_col, highlightthickness=0)
canvas_compare1.pack(side=tk.LEFT, pady=10)

canvas_compare2 = tk.Canvas(frame_compare, bg = "white", width = 1280/2, height = 400, background = background_col, highlightthickness=0)
canvas_compare2.pack(side=tk.RIGHT, pady=10)

compare_init_btn = tk.Button(frame_compare, text="Compare", font=font, command=showAnimationCompare)
compare_init_btn.pack(padx=15, pady=0)

compare_pre_btn1 = tk.Button(frame_compare, text="Prev 1", font=font, command=prevStep1)
compare_pre_btn1.pack(padx=15, pady=0)

compare_next_btn1 = tk.Button(frame_compare, text="Next 1", font=font, command=nextStep1)
compare_next_btn1.pack(padx=15, pady=0)

compare_pre_btn2 = tk.Button(frame_compare, text="Prev 2", font=font, command=prevStep2)
compare_pre_btn2.pack(padx=15, pady=0)

compare_next_btn2 = tk.Button(frame_compare, text="Next 2", font=font, command=nextStep2)
compare_next_btn2.pack(padx=15, pady=0)

# Main Control Buttons

def compareBack():
    frame_compare.pack_forget()
    frame_start.pack(pady=10)

compare_back_btn = tk.Button(frame_compare, text="Back", font=font, command=compareBack)
compare_back_btn.pack(padx=15, pady=30)

# Add the button to main menu
compare_btn = tk.Button(frame_start, text = "Compare Algorithms", font = font, command = copmareAlgos)
compare_btn.pack(side=tk.TOP, padx=10, pady=10)



# MAIN LOOP
root.mainloop()