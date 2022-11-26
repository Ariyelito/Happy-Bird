'''
Explication du scroll ici
https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame
'''
import pygame
import random
from obstacle import *


class ArrierePlan(pygame.sprite.Sprite):

   

    def __init__(self, xpos):

        #VARIABLES
        self.SCREEN_WIDHT = 640
        self.SCREEN_HEIGHT = 480
        self.GAME_SPEED = 15

        self.GROUND_HEIGHT= 640
        self.PIPE_GAP = 150

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((self.SCREEN_WIDHT, self.SCREEN_HEIGHT))
        self.image = pygame.image.load('img/background/flappy_bird_bg3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (2*640, 100))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = self.SCREEN_HEIGHT - self.GROUND_HEIGHT

    def update(self):
        self.rect[0] -= self.GAME_SPEED

    def is_off_screen(self,sprite):
         return sprite.rect[0] < -(sprite.rect[2])

    def get_random_pipes(self,xpos):
        size = random.randint(100, 300)
        pipe = Obstacle(False, xpos, size)
        pipe_inverted = Obstacle(True, xpos, self.SCREEN_HEIGHT - size - self.PIPE_GAP)
        return pipe, pipe_inverted
