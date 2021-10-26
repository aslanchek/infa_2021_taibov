import pygame
import Ball
from ast import literal_eval
from Constants import *



class Main():
    '''Главный класс игры, где определяются такие методы как рендеринг всего, главный цикл, сохранение прогресса игры'''
    def __init__(self, screen, playerName):
        '''Объявление параметров игры'''
        self.screen = screen
        self.running = True

        self.playerName = playerName
        self.playerScore = 0

        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.counter = 10
        self.objects = [] # массив в котором содержатся все летающие объекты (в частности шарики)
        self.main_loop()

    def save(self):
        '''Сохранение прогресса'''
        try:
            with open('score.txt', 'r') as f:
                data = f.read()

                if data == '':
                    data = {}
                else:
                    data = literal_eval(data)

                if self.playerName in data:
                    if self.playerScore > int(data[self.playerName]):
                        print(f"New score by {self.playerName}!") 
                        data[self.playerName] = self.playerScore
                else:
                    data[self.playerName] = self.playerScore
                    print(f"New score by {self.playerName}!")
        except FileNotFoundError: # обработка случая, когда файл записи рекордов отсуствует
            with open('score.txt', 'x') as f:
                    data = {}
                    print(f"New score by {self.playerName}!") 
                    data[self.playerName] = self.playerScore
                    with open("score.txt", "w") as f:
                        f.write(str(data))

        with open("score.txt", "w") as f:
                f.write(str(data))


    def handle_events(self):
        '''Обработчик действий игрока'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.USEREVENT:
                self.counter -= 1 # обратный отсчет
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for j in self.objects:
                    if abs(event.pos[0] - j.x) < j.r and abs(event.pos[1] - j.y) < j.r:
                        j.remove()
                        self.playerScore += 1



    def main_render(self):
        self.screen.fill(BLACK)
        for i in self.objects:
            i.render(screen)    
        screen.blit(self.myfont.render(f'Score: {self.playerScore}', False, (255, 255, 255)) ,(10,10))
        screen.blit(self.myfont.render(f'Time: {self.counter}', False, (255, 255, 255)) ,(300,10))



        pygame.display.flip()

    def main_loop(self):
        '''Основной цикл программы'''

        for i in range(15):
            self.objects.append(Ball.Ball(self)) # добавление на экран 15 шариков

        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)


        while self.running:
            clock.tick(FPS)
            for i in self.objects:
                i.move()

            self.handle_events()
            self.main_render()

            if len(self.objects) == 0 or self.counter == 0:
                self.save()
                self.running = False




def start():
    '''Простой интерфейс'''
    print("========================================")
    choice = input('enter number to select:\n 1 - start the game \n 2 - show the high score table \n >>>')
    if choice == '1':
        global player_name, screen, game
        player_name = input("input player name>>>")
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        game = Main(screen, player_name)
    elif choice == '2':
        try:
            with open('score.txt', 'r') as f:
                data = literal_eval(f.read())

                for i in data:
                    print(f"{i} ---------------- {data[i]}")
                start()


        except FileNotFoundError: # обработка случая, когда файл рекордов отсутствует
            print("there is no record file \nplay firstly")
            start()

start()