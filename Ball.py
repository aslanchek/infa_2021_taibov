import pygame
from Constants import *
from random import randint

class Ball():
    def __init__(self, game):
        self.game = game

        self.r = randint(10, 100)
        self.x = randint(self.r, SCREEN_WIDTH-self.r)
        self.y = randint(self.r, SCREEN_HEIGHT-self.r)
        self.Vx = randint(1, 10)
        self.Vy = randint(1, 10)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.Vx
        self.y += self.Vy

        if self.x + self.r > SCREEN_WIDTH or self.x - self.r < 0: 
            self.Vx *= -1

        if self.y + self.r > SCREEN_HEIGHT or self.y - self.r < 0: 
            self.Vy *= -1

    def remove(self):
        self.game.objects.remove(self)