import pygame
import numpy as np 


class Slider:
    RADIUS = 15

    def __init__(self,screen,x,y,width):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.knobX = x
        

    def getValue(self):
        if(self.x == self.knobX):
            return 0
        return (self.knobX - self.x)/(self.width)


    def isHovered(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        distance = np.sqrt(np.square(mouseX - self.knobX) + np.square(mouseY - self.y))
        if distance < Slider.RADIUS:
            return True
        return False


    def move(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        if mouseX < self.x:
            self.knobX = self.x
        elif mouseX > self.x + self.width:
            self.knobX = self.x + self.width
        else:
            self.knobX = mouseX
    
    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.width,2])
        pygame.draw.circle(self.screen,(230,230,230),(self.knobX,self.y),Slider.RADIUS)
