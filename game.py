import pygame
from menu import *
from players import X
import time
from board import Board

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.TTTX, self.TTTY = 700, 500
        self.tictactoeImg = pygame.image.load('assets/tictactoe.png')
        self.tictactoeImg = pygame.transform.scale(self.tictactoeImg, (500,500))
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'Pixeboy.ttf'
        self.player1 = X()
        self.player2 = O()
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.selection = SelectionMenu(self)
        self.curr_menu = self.main_menu
        self.matrix = [[" "," "," "], [" "," "," "], [" "," "," "]]

    def draw_opponent(self, pos):
        if pos == [0, 0]:
            self.tictactoeImg.blit(self.player2.Img(), (40,40))
        if pos == [0, 1]:
            self.tictactoeImg.blit(self.player2.Img(), (170,40))
        if pos == [0, 2]:
            self.tictactoeImg.blit(self.player2.Img(), (310,40))
        if pos == [1, 0]:
            self.tictactoeImg.blit(self.player2.Img(), (40,190))
        if pos == [1, 1]:
            self.tictactoeImg.blit(self.player2.Img(), (170,190))
        if pos == [1, 2]:
            self.tictactoeImg.blit(self.player2.Img(), (310,190))
        if pos == [2, 0]:
            self.tictactoeImg.blit(self.player2.Img(), (40,350))
        if pos == [2, 1]:
            self.tictactoeImg.blit(self.player2.Img(), (170,350))
        if pos == [2, 2]:
            self.tictactoeImg.blit(self.player2.Img(), (310,350))

    def selected_square(self):
        mouse_click = pygame.mouse.get_pressed()
        mposx, mposy = pygame.mouse.get_pos()
        b = Board()

        #Drawing player position inside the board screen
        if mouse_click[0] == True:
            if mposx in range(156,328) and mposy in range(52, 212):
                self.matrix = b.play(*self.matrix, pos = [0,0], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (40,40))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(337,468) and mposy in range(52, 212):
                self.matrix = b.play(*self.matrix, pos = [0,1], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (170,40))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(475,647) and mposy in range(52, 212):
                self.matrix = b.play(*self.matrix, pos = [0,2], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (310,40))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(156,328) and mposy in range(225, 380):
                self.matrix = b.play(*self.matrix, pos = [1,0], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (40,190))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(337,468) and mposy in range(225, 380):
                self.matrix = b.play(*self.matrix, pos = [1,1], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (170,190))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(475,647) and mposy in range(225, 380):
                self.matrix = b.play(*self.matrix, pos = [1,2], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (310,190))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(156,328) and mposy in range(391, 552):
                self.matrix = b.play(*self.matrix, pos = [2,0], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (40,350))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(337,468) and mposy in range(391, 552):
                self.matrix = b.play(*self.matrix, pos = [2,1], player =  self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (170,350))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)
            if mposx in range(475,647) and mposy in range(391, 552):
                self.matrix = b.play(*self.matrix, pos = [2,2], player = self.player1.character)
                self.tictactoeImg.blit(self.player1.Img(), (310,350))
                time.sleep(0.2)
                self.draw_opponent(b.bestAction(*self.matrix, player = self.player2.character))
                time.sleep(0.2)
                self.matrix = b.play(*self.matrix, pos = b.bestAction(*self.matrix, player = self.player2.character), player = self.player2.character)

    #Game event loop
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.WHITE)
            self.window.blit(self.display, (0,0))
            #creating the playing board
            self.tictactoe()
            #only for testing purpose
            mouse_pos = pygame.mouse.get_pos()
            # print (mouse_pos)

            self.selected_square()
            #update screen
            pygame.display.update()
            self.reset_keys()

    def tictactoe(self):
        self.window.blit(self.tictactoeImg, (self.DISPLAY_W/2 - self.TTTX/2 + 100, self.DISPLAY_H/2 - self.TTTY/2))

    #check button pressed on menu screen
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    #set button pressed back to false
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y, color = ( 255, 255, 255)):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
