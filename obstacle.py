'''
Created on 27 avr. 2022

@author: gills
'''
import pygame
import random

class Obstacle(pygame.sprite.Sprite):

   

    def __init__(self, inverted, xpos, ysize):

        #VARIABLES
        SCREEN_WIDHT = 640
        SCREEN_HEIGHT = 480

        PIPE_WIDHT = 80
        PIPE_HEIGHT = 500

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self. image = pygame.image.load('img/background/Obstacle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDHT, PIPE_HEIGHT))


        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize


        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.rect[0] -= 15