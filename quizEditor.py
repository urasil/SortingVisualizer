import tkinter as tk
from tkinter.filedialog import askopenfilename,askdirectory
import os
from quizManager import Quiz
import tkinter.font as tkFont

#Usage: To add this Frame into the main program, a QuizEditorFrame needs to be initialised, e.g. frame = QuizEditorFrame(window). 
#When the Frame is initialised, font-typeface and font-size are optional parameters to be modified.


class QuizEditorFrame(tk.Frame):   #create a frame for the quiz editor
    
    def __clearAllInput(self):   #clear all existing text field
        self.questionEntry.delete(0, tk.END)
        self.imagePath.set('')
        self.choiceAmountVar.set('4')
        self.__updateChoiceAmount(self.choiceAmountVar.get())
        self.choice_1_Entry.delete(0, tk.END)   
        self.choice_2_Entry.delete(0, tk.END)
        self.choice_3_Entry.delete(0, tk.END)
        self.choice_4_Entry.delete(0, tk.END)
        self.answerEntry.delete(0, tk.END)
        self.explanationEntry.delete(0,tk.END)
        
    def __selectFile(self): # a function to read file path
        path_ = askopenfilename()
        if path_:
            self.filePath.set(path_)
            self.__clearAllInput()
            file = Quiz()
            file.quizRead(path_)
            question,imageLink,choices,answer,explanation = file.getQuiz()
            if question:
                self.questionEntry.insert(0,question)
            if imageLink:
                self.imagePath.set(imageLink)
            if choices:
                size = len(choices)
                if size >= 2:
                    self.choiceAmountVar.set(str(size))
                    self.__updateChoiceAmount(str(size))
                if size == 4:
                    self.choice_1_Entry.insert(0,choices[0])
                    self.choice_2_Entry.insert(0,choices[1])
                    self.choice_3_Entry.insert(0,choices[2])
                    self.choice_4_Entry.insert(0,choices[3])
                elif size == 3:
                    self.choice_1_Entry.insert(0,choices[0])
                    self.choice_2_Entry.insert(0,choices[1])
                    self.choice_3_Entry.insert(0,choices[2])
                elif size == 2:
                    self.choice_1_Entry.insert(0,choices[0])
                    self.choice_2_Entry.insert(0,choices[1])
                elif size == 1:
                    self.choice_1_Entry.insert(0,choices[0])
                
            if answer:
                self.answerEntry.insert(0,answer)
            if explanation:
                self.explanationEntry.insert(0,explanation)
            
    
    def __selectDirectory(self):   # a function to read directory path
        directory_ = askdirectory(initialdir=os.path.abspath(__file__))
        if directory_:
            self.filePath.set(self.__newFilePath(directory_))
            self.__clearAllInput()
        
    def __newFilePath(self,directory):   #generate an unused file name
        num = 1
        newName = '/' + self.fileNamePrefix + str(num) + '.txt'
        while(os.path.exists(directory+newName)):
            num += 1
            newName = '/' + self.fileNamePrefix + str(num) + '.txt'
        
        return directory+newName    #new path with new file name
    
    def __selectImage(self): # a function to read image path
        path_ = askopenfilename()
        if path_:
            self.imagePath.set(path_)
            
    def __updateChoiceAmount(self,choiceAmount):
        self.choice_1_Label.grid_forget()   #Initially hide all choice widgets
        self.choice_1_Entry.grid_forget()
        self.choice_2_Label.grid_forget()
        self.choice_2_Entry.grid_forget()
        self.choice_3_Label.grid_forget()
        self.choice_3_Entry.grid_forget()
        self.choice_4_Label.grid_forget()
        self.choice_4_Entry.grid_forget()
        if choiceAmount == '4':
            self.choice_1_Label.grid(row=3,column=0)
            self.choice_1_Entry.grid(row=3,column=1,sticky='W')
            self.choice_2_Label.grid(row=3,column=2)
            self.choice_2_Entry.grid(row=3,column=3,sticky='W')
            self.choice_3_Label.grid(row=4,column=0)
            self.choice_3_Entry.grid(row=4,column=1,sticky='W')
            self.choice_4_Label.grid(row=4,column=2)
            self.choice_4_Entry.grid(row=4,column=3,sticky='W')
        elif choiceAmount == '3':
            self.choice_1_Label.grid(row=3,column=0)
            self.choice_1_Entry.grid(row=3,column=1,sticky='W')
            self.choice_2_Label.grid(row=3,column=2)
            self.choice_2_Entry.grid(row=3,column=3,sticky='W')
            self.choice_3_Label.grid(row=4,column=0)
            self.choice_3_Entry.grid(row=4,column=1,sticky='W')
            
        elif choiceAmount == '2':
            self.choice_1_Label.grid(row=3,column=0)
            self.choice_1_Entry.grid(row=3,column=1,sticky='W')
            self.choice_2_Label.grid(row=3,column=2)
            self.choice_2_Entry.grid(row=3,column=3,sticky='W')
            
    def __saveFile(self):
        question = self.questionEntry.get()
        imageLink = self.imagePath.get()
        answer = self.answerEntry.get()
        explanation = self.explanationEntry.get()
        choice_1 = None
        choice_2 = None
        choice_3 = None
        choice_4 = None
        if self.choiceAmountVar.get() == '4':
            choice_1 = self.choice_1_Entry.get()
            choice_2 = self.choice_2_Entry.get()
            choice_3 = self.choice_3_Entry.get()
            choice_4 = self.choice_4_Entry.get()
        elif self.choiceAmountVar.get() == '3':  
            choice_1 = self.choice_1_Entry.get()
            choice_2 = self.choice_2_Entry.get()
            choice_3 = self.choice_3_Entry.get()
        elif self.choiceAmountVar.get() == '2': 
            choice_1 = self.choice_1_Entry.get()
            choice_2 = self.choice_2_Entry.get()
        
        quiz = Quiz(question=question, imageLink=imageLink, choice_1=choice_1,choice_2=choice_2,
                    choice_3=choice_3,choice_4=choice_4,answer=answer,explanation=explanation)
        
        quiz.quizWrite(self.filePath.get())
        
    '''
    def __checkFont(self,font_typeface, font_size):
        try:
            tkFont.Font(font=font_typeface)
        except tk.TclError:
            return False
        
        try:
            font_size = int(font_size)
            return font_size>0
        except ValueError:
            return False
    '''     
    
    def __init__(self,master=None,font_typeface='Roboto-Light',font_size=16):  
        super().__init__(master)
        
        '''
        if self.__checkFont(font_typeface,font_size):
            self.font = (font_typeface,font_size)   #default font
        else:
            self.font = ("Helvetica",16)
        '''
        self.font = (font_typeface,font_size)
            
        self.fileNamePrefix = "newQuiz_"   #default prefix of a new file name
        self.filePath = tk.StringVar()  #indicate the path of quiz file
        self.pathLabel_1 = tk.Label(self,text="File Path:",font=self.font).grid(row=0,column=0)
        self.pathLabel_2 = tk.Label(self,textvariable=self.filePath,width=20,anchor='e',font=self.font).grid(row=0,column=1,columnspan=2)
        self.newButton = tk.Button(self,text='New',command=self.__selectDirectory,font=self.font)
        self.loadButton_1 = tk.Button(self,text='Load',command=self.__selectFile,font=self.font)
        self.saveButton = tk.Button(self,text='Save',command=self.__saveFile,font=self.font)
        self.newButton.grid(row=0,column=2,sticky='w') #read a path of the directory for saving the new file
        self.loadButton_1.grid(row=0,column=3,sticky='w')  #read the path of an existing file
        self.saveButton.grid(row=0,column=4,sticky='w') 
        #self.newButton.pack(side=tk.LEFT)
        #self.loadButton_1.pack(side=tk.LEFT)
        #self.saveButton.pack(side=tk.LEFT)
    
    
        self.questionLabel = tk.Label(self,text="Question:",justify='left',font=self.font)
        self.questionEntry = tk.Entry(self,width=50,font=self.font)
        self.questionLabel.grid(row=1,column=0)
        self.questionEntry.grid(row=1,column=1)
    
        self.choiceAmountVar = tk.StringVar()
        self.choiceAmountVar.set('4')   #default amount is 4
        self.choiceAmountLabel = tk.Label(self,text="Choice Amount:",font=self.font)
        self.choiceAmount = tk.OptionMenu(self,self.choiceAmountVar,'2','3','4',command=self.__updateChoiceAmount)
        self.choiceAmount["menu"].config(font = self.font)
        self.choiceAmountLabel.grid(row=1,column=2)
        self.choiceAmount.grid(row=1,column=3,sticky='W')
        
        self.imagePath = tk.StringVar()
        self.imagePathLabel_1 = tk.Label(self,text="Image Path:",font=self.font)
        self.imagePathLabel_2 = tk.Label(self,textvariable=self.imagePath,width=30,anchor='e',font=self.font)
        self.loadButton_2 = tk.Button(self,text='Load',command=self.__selectImage,font=self.font).grid(row=2,column=2,sticky='W')
        self.imagePathLabel_1.grid(row=2,column=0)
        self.imagePathLabel_2.grid(row=2,column=1)
        
        self.choice_1_Label = tk.Label(self,text="Choice 1",font=self.font)
        self.choice_2_Label = tk.Label(self,text="Choice 2",font=self.font)
        self.choice_3_Label = tk.Label(self,text="Choice 3",font=self.font)
        self.choice_4_Label = tk.Label(self,text="Choice 4",font=self.font)
        self.choice_1_Entry = tk.Entry(self,font=self.font)
        self.choice_2_Entry = tk.Entry(self,font=self.font)
        self.choice_3_Entry = tk.Entry(self,font=self.font)
        self.choice_4_Entry = tk.Entry(self,font=self.font)
        
        self.__updateChoiceAmount(self.choiceAmountVar.get())
    
    
        self.answerLabel = tk.Label(self,text="Answer Choice:",font=self.font)
        self.answerEntry = tk.Entry(self,width=2,font=self.font)
        self.answerLabel.grid(row=5,column=0)
        self.answerEntry.grid(row=5,column=1,sticky='W')
        
        self.explanationLabel = tk.Label(self,text="Explanation:",font=self.font)
        self.explanationEntry = tk.Entry(self,width=50,font=self.font)
        self.explanationLabel.grid(row=6,column=0)
        self.explanationEntry.grid(row=6,column=1,sticky='W')
    

if __name__ == '__main__':    #the code below is only for debugging
    window = tk.Tk()   #start a window
    window.title('Quiz Editor')  
    window.geometry('1280x720')
    frame1 = QuizEditorFrame(window)
    frame1.pack()
    
    window.mainloop()