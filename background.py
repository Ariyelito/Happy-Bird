import pygame
import random
from obstacle import *


class sol(pygame.sprite.Sprite):
    
    def __init__(self, xpos):

        self.LARGEUR_ECRAN = 640
        self.HAUTEUR_ECRAN = 480
        self.VITESSE_JEU = 15

        self.HAUTEUR_SOL= 102
        self.ESPACE_OBSTACLE = 150

        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.display.set_mode((self.LARGEUR_ECRAN, self.HAUTEUR_ECRAN))
        self.image = pygame.image.load('img/background/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (3 * self.HAUTEUR_ECRAN, self.HAUTEUR_SOL))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = self.HAUTEUR_ECRAN - self.HAUTEUR_SOL

    def update(self):
        self.rect[0] -= self.VITESSE_JEU

    def hors_ecran(self,sprite):
         return sprite.rect[0] < -(sprite.rect[2])

    def obstacle_aleatoire(self,xpos):
        hauteur = random.randint(102, 300)
        obstacle = Obstacle(False, xpos, hauteur)
        obstacle_inverse = Obstacle(True, xpos, self.HAUTEUR_ECRAN - hauteur - self.ESPACE_OBSTACLE)
        return obstacle, obstacle_inverse