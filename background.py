'''
Explication du scroll ici
https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame
'''
import pygame
import random
from obstacle import *


class ArrierePlan(pygame.sprite.Sprite):
    
    def __init__(self, xpos):

        self.LARGEUR_ECRAN = 640
        self.HAUTEUR_ECRAN = 480
        self.VITESSE_JEU = 15

        self.HAUTEUR_ARRIEREPLAN= 640
        self.ESPACE_OBSTACLE = 150

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((self.LARGEUR_ECRAN, self.HAUTEUR_ECRAN))
        self.image = pygame.image.load('img/background/flappy_bird_bg3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (2*640, 100))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = self.HAUTEUR_ECRAN - self.HAUTEUR_ARRIEREPLAN

    def update(self):
        self.rect[0] -= self.VITESSE_JEU

    def is_off_screen(self,sprite):
         return sprite.rect[0] < -(sprite.rect[2])

    def get_random_obstacle(self,xpos):
        hauteur = random.randint(100, 300)
        obstacle = Obstacle(False, xpos, hauteur)
        obstacle_inverse = Obstacle(True, xpos, self.HAUTEUR_ECRAN - hauteur - self.ESPACE_OBSTACLE)
        return obstacle, obstacle_inverse
