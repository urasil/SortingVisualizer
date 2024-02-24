import random

#This will be a slider
#No need for a lower bound 
#We can simply say that there should at least be 5 elements in the list for better visualisation

sliderUpper = int(input("Enter the upper bound: "))
MAX = 100

def randomListGen():
    lst = []
    for i in range(5, sliderUpper+1):
        lst.append(random.randint(1,MAX))
    return lst

print(randomListGen())