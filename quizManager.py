class Quiz():
    # 4 constructors represent 4 different situations, cause the number of choices might be different
    '''
    def __init__(self) -> None:
        self.__question = None
        self.__choices = []     
        self.__answer = None     
        self.__imageLink = None    
    def __init__(self,question,imageLink,choice_1,choice_2,answer):    
        self.__question = question
        self.__choices = []
        self.__choices.append(choice_1)
        self.__choices.append(choice_2)
        self.__answer = answer
        self.__imageLink = imageLink
        
    def __init__(self,question,imageLink,choice_1,choice_2,choice_3,answer):
        self.__question = question
        self.__choices = []
        self.__choices.append(choice_1)
        self.__choices.append(choice_2)
        self.__choices.append(choice_3)
        self.__answer = answer
        self.__imageLink = imageLink
    '''
    def __init__(self,question=None,imageLink=None,choice_1=None,choice_2=None,choice_3=None,choice_4=None,answer=None,explanation=None) -> None:
        if question is not None:
            self.__question = question
        self.__choices = []   #Be careful the index of choices, range of number of choices is 2 - 4
        if choice_1 is not None:
            self.__choices.append(choice_1)
        if choice_2 is not None:
            self.__choices.append(choice_2)
        if choice_3 is not None:
            self.__choices.append(choice_3)
        if choice_4 is not None:
            self.__choices.append(choice_4)
        if answer is not None:
            self.__answer = answer   #answer is actually the (index of choices + 1)
        if imageLink is not None:
            self.__imageLink = imageLink  #At console development stage, image link would be returned as a string for testing
        if explanation is not None:
            self.__explanation = explanation
        
    def quizRead(self,filePath):    #given a filePath, this function reads question, image link, 4 choices, and corrent choice from the file
        try:
            
            file = open(filePath,"r")
            for line in file:
                if "Quest" in line:
                    self.__question = line.split('=')[1].strip()[1:-1]
                elif "Image" in line:
                    self.__imageLink = line.split('=')[1].strip()[1:-1]
                elif "Choice" in line:
                    self.__choices.append(line.split('=')[1].strip()[1:-1])
                elif "Answer" in line:
                    self.__answer = line.split('=')[1].strip()[1:-1]
                elif "Explanation" in line:
                    self.__explanation = line.split('=')[1].strip()[1:-1]
            file.close()
        except FileNotFoundError:
            print("File not found")
        
    def getQuiz(self):   #return the whole quiz
        return(self.__question,self.__imageLink,self.__choices,self.__answer,self.__explanation)

    def quizWrite(self,filePath):   #given a filePath, write quiz into a new/existing file
        try:
            file = open(filePath,"w")
            writtenList = []
            choiceAmount = len(self.__choices)
            writtenList.append("Quest="+'"'+self.__question+'"'+"\n")
            writtenList.append("Image="+'"'+self.__imageLink+'"'+"\n")
            for i in range(choiceAmount):
                writtenList.append("Choice_"+ str(i+1) + "=" + '"'+self.__choices[i]+'"'+"\n")
            writtenList.append("Answer=" + '"'+self.__answer+'"'+"\n")
            writtenList.append("Explanation=" + '"' + self.__explanation + '"' + "\n")
            file.writelines(writtenList)
            file.close()
            
        except PermissionError:
            print("No permission to write files")
        
        except FileNotFoundError:
            print("Path not exist")
            
        
        
if __name__ == '__main__':   #the code below is only for debugging
    quiz = Quiz()
    quiz.quizRead("./quizLibrary/quiz_template.txt")
    print(quiz.getQuiz())
    #quiz.quizWrite("./quizLibrary/quiz_test.txt")
    
    
      
    
    
    