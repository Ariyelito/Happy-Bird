import pygame
from background import *
from bird import *


pygame.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Flappy Bird made by Ricardo!")

arriere_plan = ArrierePlan(640, 480)
bird = Bird()
#obstacle = Boite()

running = True

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
      #  print("CollisionS")

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()