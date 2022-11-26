'''
Created on 27 avr. 2022

@author: gills
'''
import pygame

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images =  [pygame.image.load('img/bird/bird (1).png').convert_alpha(),]

        self.speed = 20

        self.current_image = 0
        self.image = pygame.image.load('img/bird/bird (1).png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 480 / 6
        self.rect[1] = 640 / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += 2.5

        #UPDATE HEIGHT
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -20

    def begin(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
