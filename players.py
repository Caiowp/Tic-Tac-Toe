import pygame

class X():
    def __init__(self):
        self.XImg = pygame.image.load('assets/x.png')
        self.character = 'X' #'

    def character(self):
        return self.character

    def Img(self):
        return self.XImg

class O():
    def __init__(self):
        self.OImg = pygame.image.load('assets/o.png')
        self.character = 'O' #'

    def character(self):
        return self.character

    def Img(self):
        return self.OImg
