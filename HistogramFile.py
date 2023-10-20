import numpy as np
import pygame
from SliderFile import Slider
from ButtonFile import Button


class Histogram:
    ASCENDING = 0
    DESCENDING = 1

    BUBBLE_SORT = 2
    SELECTION_SORT = 3

    MAX_CNT = 40
    MIN_CNT = 10

    MAX_VAL = 100

    MAX_HEIGHT_IN_PIXELS = 300

    WAIT_TIME = 40

    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        
        self.numbers = []

        self.currentlySorting = False
        self.order = Histogram.ASCENDING
        self.algorithm = Histogram.SELECTION_SORT 

        self.slider = Slider(self.screen,650,150,300)
        
        self.greenHighlight = -1
        self.redHighlight = -1

        self.reset()


    def isBusy(self):
        return self.currentlySorting


    def handleEvent(self,buttonLabel):
        if self.slider.isHovered():
            self.slider.move()
            self.reset()
            return

        if buttonLabel == "None":
            return
        
        if buttonLabel == "Selection sort":
            self.algorithm = Histogram.SELECTION_SORT
        elif buttonLabel == "Bubble sort":
            self.algorithm = Histogram.BUBBLE_SORT
        
        elif buttonLabel == "Ascending":
            self.order = Histogram.ASCENDING
        elif buttonLabel == "Descending":
            self.order = Histogram.DESCENDING
        
        elif buttonLabel == "Start":
            self.currentlySorting = True
            if self.algorithm == Histogram.BUBBLE_SORT:
                self.bubbleSort()
            else:
                self.selectionSort()
            self.currentlySorting = False


    def reset(self):
        percent = self.slider.getValue()
        cnt = Histogram.MAX_CNT - int(percent*(Histogram.MAX_CNT - Histogram.MIN_CNT))
        self.numbers = np.random.randint(0,Histogram.MAX_VAL,cnt)



    def draw(self):
        self.slider.draw()

        rectWidth = np.floor(self.width/len(self.numbers))

        for i in range(len(self.numbers)):
            rectHeight = np.ceil(Histogram.MAX_HEIGHT_IN_PIXELS * (self.numbers[i]/Histogram.MAX_VAL))
            pygame.draw.rect(self.screen,(130,130,200),[i*rectWidth,self.height - rectHeight,rectWidth-2,rectHeight])

        if self.greenHighlight != -1 and self.redHighlight != -1:
            # Green highlight
            rectHeight = np.ceil(Histogram.MAX_HEIGHT_IN_PIXELS * (self.numbers[self.greenHighlight]/Histogram.MAX_VAL))
            pygame.draw.rect(self.screen,(0,130,0),[self.greenHighlight*rectWidth,self.height - rectHeight,rectWidth-2,rectHeight])

            # Red highlight
            rectHeight = np.ceil(Histogram.MAX_HEIGHT_IN_PIXELS * (self.numbers[self.redHighlight]/Histogram.MAX_VAL))
            pygame.draw.rect(self.screen,(130,0,0),[self.redHighlight*rectWidth,self.height - rectHeight,rectWidth-2,rectHeight])



    def bubbleSort(self):
        from main import checkForEvents

        n = len(self.numbers)
        
        for i in range(n):
            swapped = False
            
            for j in range(0, n-i-1):
                self.greenHighlight = j
                self.redHighlight = j - 1
                checkForEvents()
                pygame.time.wait(Histogram.WAIT_TIME)
                

                if self.checkCondition(j,j+1):
                    self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]
                    swapped = True
                
            if (swapped == False):
                break
        
        self.greenHighlight = -1
        self.redHighlight = -1

    
    def selectionSort(self):
        from main import checkForEvents

        for i in range(len(self.numbers)):
            min_idx = i
            for j in range(i+1, len(self.numbers)):
                
                if self.checkCondition(min_idx,j):
                    min_idx = j

                self.greenHighlight = min_idx
                self.redHighlight = j                
                checkForEvents()
                pygame.time.wait(Histogram.WAIT_TIME)           

            self.numbers[i], self.numbers[min_idx] = self.numbers[min_idx], self.numbers[i]

        self.greenHighlight = -1
        self.redHighlight = -1

    
    def checkCondition(self,i,j):
        if self.algorithm == Histogram.BUBBLE_SORT:
            
            if self.order == Histogram.ASCENDING:
                return self.numbers[i] > self.numbers[j]
            else:
                return self.numbers[i] < self.numbers[j]

        else:
            
            if self.order == Histogram.ASCENDING:
                return self.numbers[i] > self.numbers[j]
            else:
                return self.numbers[i] < self.numbers[j]