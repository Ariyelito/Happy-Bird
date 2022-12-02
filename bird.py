'''
Created on 27 avr. 2022

@author: gills
'''
import pygame

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        
        LARGEUR_ECRAN = 640
        HAUTEUR_ECRAN = 480

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

        self.vitesse = 20

        self.image = pygame.image.load('img/bird/bird (1).png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0, 0.4)

        self.rect = self.image.get_rect()

        #fixer l'image sur l'écran
        self.rect[0] = LARGEUR_ECRAN / 6
        self.rect[1] = HAUTEUR_ECRAN / 2

    def update(self):
        self.vitesse += 2.5
        self.rect[1] += self.vitesse

    def saut(self):
        self.vitesse = -10


