import pygame
import Ball
from Constants import *



class Main():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.objects = []
        self.main_loop()
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                print('Click!')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print("added ball")
                    self.objects.append(Ball.Ball(self))
                    print(self.objects)

    def main_render(self):
        self.screen.fill(BLACK)
        for i in self.objects:
            i.render(screen)
        pygame.display.flip()

    def main_loop(self):
        '''Основной цикл программы'''
        pygame.display.update()
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(FPS)
            for i in self.objects:
                i.move()
            self.handle_events()
            self.main_render()






pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)