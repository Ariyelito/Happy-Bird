'''
Created on 27 avr. 2022

@author: gills
'''
import pygame

class Bird(pygame.sprite.Sprite):

  


    def __init__(self):

        #VARIABLES
        SCREEN_WIDHT = 640
        SCREEN_HEIGHT = 480

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

        self.speed = 20

        self.current_image = 0
        self.image = pygame.image.load('img/bird/bird (1).png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0, 0.5)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDHT / 6
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.speed += 2.5

        #UPDATE HEIGHT
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -20

    def begin(self):
        self.current_image = (self.current_image + 1) % 3

