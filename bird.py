'''
Created on 27 avr. 2022

@author: gills
'''
import pygame

class Bird:
    def __init__(self):
        self.angle = 0
        self.echelle = 0.7
        self.image = pygame.image.load('img/bird/bird (1).png')
        self.image = pygame.transform.rotozoom(self.image, self.angle, self.echelle)
        self.pos_x = 50
        self.pos_y = 325
        self.saut = False
        self.saut_duree = 30
        self.saut_temps = 0
        self.gravite = 1
        self.rect = False

    def dessiner(self, screen):
        self.rect = screen.blit(self.image, (self.pos_x, self.pos_y))
        if self.pos_y < 325:
            self.pos_y += self.gravite
        if self.saut:
            self.pos_y -= 4
            self.saut_temps += 1
            if self.saut_temps > 40:
                self.saut = False
                self.saut_temps = 0

    def detect_collision(self, rect):
        if self.rect.colliderect(rect):
            return True
        return False
