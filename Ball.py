import pygame
from Constants import *
from random import randint

class Ball():
    def __init__(self, game):
        '''инициализация класса Ball'''
        self.game = game

        self.r = randint(20, 50)
        self.x = randint(self.r, SCREEN_WIDTH-self.r)
        self.y = randint(self.r, SCREEN_HEIGHT-self.r)
        self.Vx = randint(-10, 10)
        self.Vy = randint(-10, 10)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def render(self, screen):
        '''отрисовка шарика'''
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        '''метод который отвечает за движение шарика и случайный отскок от стенок'''
        self.x += self.Vx
        self.y += self.Vy

        if self.x + self.r > SCREEN_WIDTH:
            self.Vx = randint(-10, 0)
            self.Vy = randint(-10, 10)

        if self.x - self.r < 0: 
            self.Vx = randint(0, 10)
            self.Vy = randint(-10, 10)


        if self.y + self.r > SCREEN_HEIGHT:
            self.Vx = randint(-10, 10)
            self.Vy = randint(-10, 0)
        if self.y - self.r < 0: 
            self.Vx = randint(-10, -10)
            self.Vy = randint(0, 10)

    def remove(self):
        '''удаление шарика'''
        self.game.objects.remove(self)