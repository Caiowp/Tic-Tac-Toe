import pygame

class X():
    def __init__(self):
        self.XImg = pygame.image.load('assets/x.png')

    def Img(self):
        return self.XImg

class O():
    def __init__(self):
        self.OImg = pygame.image.load('assets/o.png')

    def Img(self):
        return self.OImg
