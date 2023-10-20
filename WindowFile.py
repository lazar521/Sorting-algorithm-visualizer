import pygame 
from ButtonFile import Button
from HistogramFile import Histogram

pygame.init()



class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Window(metaclass=SingletonMeta):
    bgColor = (0,0,0)

    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.buttons = []

        self.mousePressed = False
        self.screen = pygame.display.set_mode((self.width, self.height)) 
        pygame.display.set_caption('Sort visualizer') 

        self.histogram = Histogram(self.screen,width,height)


    def addButton(self,x,y,width,height,text):
        self.buttons.append(Button(self.screen,x,y,width,height,text))

    def pressMouse(self):
        self.mousePressed = True

    def letMouse(self):
        self.mousePressed = False

    def getMouseState(self):
        return self.mousePressed

    def draw(self):
        self.screen.fill(Window.bgColor)

        self.histogram.draw()        
        for button in self.buttons:
            button.draw()

        pygame.display.update() 



    def handleClick(self):
        buttonLabel = "None"

        for button in self.buttons:
            if button.isHovered():
                buttonLabel = button.getText()
                break

        if buttonLabel == "Quit":
            exit(0)

        if not self.histogram.isBusy():
            self.histogram.handleEvent(buttonLabel)


    
                


