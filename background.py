'''
Explication du scroll ici
https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame
'''
import pygame
import random
from obstacle import *


class ArrierePlan(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/background/flappy_bird_bg3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (2, 100))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = 640 - 480

    def update(self):
        self.rect[0] -= 15

    def is_off_screen(sprite):
         return sprite.rect[0] < -(sprite.rect[2])

    def get_random_pipes(xpos):
        size = random.randint(100, 300)
        pipe = Obstacle(False, xpos, size)
        pipe_inverted = Obstacle(True, xpos, 640 - size - 150)
        return pipe, pipe_inverted
