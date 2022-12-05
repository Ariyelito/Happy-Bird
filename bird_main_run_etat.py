import pygame
from pygame import MOUSEBUTTONUP

from background import *
from bird import *
from obstacle import *
from musique import *

pygame.init()

LARGEUR_ECRAN = 640
HAUTEUR_ECRAN = 480
pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
LARGEUR_SOL = 2 * LARGEUR_ECRAN
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 155, 0)
BACKGROUND = pygame.image.load('img/background/flappy_bird_bg3.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (LARGEUR_ECRAN, HAUTEUR_ECRAN))
BACKGROUND2 = pygame.image.load('img/background/start.png').convert_alpha()
BACKGROUND2 = pygame.transform.rotozoom(BACKGROUND2,0, 0.3)

arriere_plan = ArrierePlan(LARGEUR_SOL - 20)
screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

bird = Bird()
bird_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

HORLOGE = pygame.time.Clock()

def main():
    global font, musique

    ground_group.empty()
    pipe_group.empty()
    bird.rect[0] = LARGEUR_ECRAN / 6
    bird.rect[1] = LARGEUR_ECRAN / 2
    
    bird_group.add(bird)

    for i in range(2):
        ground = ArrierePlan(LARGEUR_SOL * i)
        ground_group.add(ground)
    
    for i in range(2):
        pipes = arriere_plan.obstacle_aleatoire(LARGEUR_ECRAN * i + 800)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    pygame.init()
    font = pygame.font.SysFont('Arial', 48)
    
    musique = Musique()
    pygame.display.update()
    pygame.display.set_caption('Happy Bird')
    while True:
        musique.jouerMusique()
        if jouer() == False:
            break


def gameoverText():
    global text, text2, textRect, text2Rect, oui, non, ouiRect, nonRect, bird
    text = font.render('Game over', True, ROUGE)
    text2 = font.render('Voulez-vous jouer encore?', True, NOIR)
    textRect = text.get_rect()
    textRect.center = (LARGEUR_ECRAN/2, HAUTEUR_ECRAN/2)

    text2 = font.render('Voulez-vous jouer encore?', True, NOIR)
    text2Rect = text2.get_rect()
    text2Rect.center = (int(LARGEUR_ECRAN / 2), int(HAUTEUR_ECRAN / 2) + 50)

    oui = font.render('Oui', True, VERT)
    ouiRect = oui.get_rect()
    ouiRect.center = (int(LARGEUR_ECRAN / 2) - 60, int(HAUTEUR_ECRAN / 2) + 110)

    non = font.render('Non', True, ROUGE)
    nonRect = non.get_rect()
    nonRect.center = (int(LARGEUR_ECRAN / 2) + 60, int(HAUTEUR_ECRAN / 2) + 110)

    # voulez vous continuer a jouer
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                print('MOUSEBUTTONUP')
                xSouris, ySouris = event.pos
                if ouiRect.collidepoint((xSouris, ySouris)):
                    main()
                elif nonRect.collidepoint((xSouris, ySouris)):
                    pygame.quit()
                    
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        screen.blit(oui, ouiRect)
        screen.blit(non, nonRect)
        pygame.display.update()
        HORLOGE.tick(15)

def jouer():
    begin = True
    
    while begin:
        
        HORLOGE.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.saut()
                    begin = False
        screen.blit(BACKGROUND, (0, 0))
        screen.blit(BACKGROUND2, (150, -100))
    

        if arriere_plan.hors_ecran(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])

            new_ground = ArrierePlan(LARGEUR_SOL - 20)
            ground_group.add(new_ground)

        ground_group.update()

        bird_group.draw(screen)
        ground_group.draw(screen)

        pygame.display.update()


    while True:
        HORLOGE.tick(15) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.saut()

        screen.blit(BACKGROUND, (0, 0))

        if arriere_plan.hors_ecran(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])

            new_ground = ArrierePlan(LARGEUR_SOL - 20)
            ground_group.add(new_ground)

        if arriere_plan.hors_ecran(pipe_group.sprites()[0]):
            pipe_group.remove(pipe_group.sprites()[0])
            pipe_group.remove(pipe_group.sprites()[0])
            pipes = arriere_plan.obstacle_aleatoire(LARGEUR_ECRAN * 2)
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])


        bird_group.update()
        ground_group.update()
        pipe_group.update()
        bird_group.draw(screen)
        pipe_group.draw(screen)
        ground_group.draw(screen)
        
        pygame.display.update()

        if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
                print('Colision')
                gameoverText()


if __name__ == '__main__':
    main()