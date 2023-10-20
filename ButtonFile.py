import pygame

pygame.init()
smallfont = pygame.font.SysFont('calibri',35) 


class Button:
    hoverColor = (170,160,200)
    baseColor = (240,240,240)

    def __init__(self, screen, x, y, width, height, text):
        self.text = text
        self.font = smallfont.render(text , True , (100,100,100)) 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen


    def getText(self):
        return self.text


    def isHovered(self):
        mouseX,mouseY = pygame.mouse.get_pos()

        if (mouseX > self.x and mouseX < self.x + self.width) and (mouseY > self.y and mouseY < self.y + self.height):
            return True
        
        return False


    def draw(self):
        mouse = pygame.mouse.get_pos() 
      
        if self.isHovered():
            color = Button.hoverColor
        else:
            color = Button.baseColor

        pygame.draw.rect(self.screen,color,[self.x,self.y,self.width,self.height])
        self.screen.blit(self.font , (self.x, self.y)) 
 
