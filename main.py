import pygame 
from ButtonFile import Button
from WindowFile import Window
pygame.init()


def checkForEvents():
    global running

    window = Window()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            window.pressMouse()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            window.letMouse()
        
        if window.getMouseState():
            window.handleClick()

    window.draw()



if __name__ == "__main__":
    height = 600
    width = 1000

    ## add button group class 

    window = Window(width,height)

    window.addButton(100,50,220,40,"Bubble sort" )
    window.addButton(350,50,220,40,"Selection sort")
    window.addButton(100,100,220,40,"Ascending")
    window.addButton(350,100,220,40,"Descending")
    window.addButton(100,150,220,40,"Start")
    window.addButton(350,150,220,40,"Quit")


    running = True
    while running:
        checkForEvents()
        
