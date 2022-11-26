<<<<<<< Updated upstream
'''
Created on 27 avr. 2022

@author: gills
'''
=======
>>>>>>> Stashed changes
import pygame
import random

class Obstacle:
    def __init__(self):
        self.angle = 0
        self.echelle = 0.8
<<<<<<< Updated upstream
        self.image = pygame.image.load('img/background/Obstacle.png')
        self.image = pygame.transform.rotozoom(self.image, self.angle, self.echelle)
        self.pos_x = 0
        self.pos_y = 135
        self.vitesse = 2
        self.rect = False
        
=======
        self.image = pygame.image.load('img/obstacle/obstacle1.png')
        self.image = pygame.transform.rotozoom(self.image, self.angle, self.echelle)
        self.pos_x = 700
        self.pos_y = 360
        self.vitesse = 2
        self.rect = False

>>>>>>> Stashed changes
    def dessiner(self, screen):
        self.rect = screen.blit(self.image, (self.pos_x, self.pos_y))
        self.pos_x -= self.vitesse
        if self.pos_x < -50:
<<<<<<< Updated upstream
            self.pos_x = random.randint(400, 500)
=======
            self.pos_x = random.randint(700, 800)
>>>>>>> Stashed changes
            self.vitesse = random.randint(2, 5)
