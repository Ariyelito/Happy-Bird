'''
Created on 27 avr. 2022

@author: gills
'''
import pygame


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, inverse, xpos, ydimenssion):

        LARGEUR_ECRAN = 640
        HAUTEUR_ECRAN = 480

        LARGEUR_OBSTACLE = 80
        HAUTEUR_OBSTACLE = 500

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        self.image = pygame.image.load('img/background/Obstacle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGEUR_OBSTACLE, HAUTEUR_OBSTACLE))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverse:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ydimenssion)
        else:
            self.rect[1] = HAUTEUR_ECRAN - ydimenssion

    def update(self):
        self.rect[0] -= 15
