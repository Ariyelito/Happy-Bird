import pygame
from background import *
from bird import *
from musique import *


pygame.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Flappy Bird made by Ricardo!")

arriere_plan = ArrierePlan(640, 480)
bird = Bird()
musique = Musique()
#obstacle = "Boite()"
running = True
musique.jouerMusique()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            bird.saut = True

    arriere_plan.dessiner(screen)
    bird.dessiner(screen)
    #obstacle.dessiner(screen)

    #if bird.detect_collision(obstacle.rect):
        #running = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()