'''
Created on 27 avr. 2022

@author: gills
'''
import pygame
import random

class Obstacle:
    def __init__(self):
        self.angle = 0
        self.echelle = 0.8
        self.image = pygame.image.load('img/background/Obstacle.png')
        self.image = pygame.transform.rotozoom(self.image, self.angle, self.echelle)
        self.pos_x = 0
        self.pos_y = 135
        self.vitesse = 2
        self.rect = False
        
    def dessiner(self, screen):
        self.rect = screen.blit(self.image, (self.pos_x, self.pos_y))
        self.pos_x -= self.vitesse
        if self.pos_x < -50:
            self.pos_x = random.randint(400, 500)
            self.vitesse = random.randint(2, 5)
