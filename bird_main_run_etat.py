import pygame
from pygame import MOUSEBUTTONUP

from background import *
from bird import *
from obstacle import *
from musique import *
# from msilib.schema import Font

LARGEUR_ECRAN = 640
HAUTEUR_ECRAN = 480
LARGEUR_SOL = 2 * LARGEUR_ECRAN
NOIR = (0, 0, 0)
BACKGROUND = pygame.image.load('img/background/flappy_bird_bg3.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (LARGEUR_ECRAN, HAUTEUR_ECRAN))

arriere_plan = ArrierePlan(LARGEUR_SOL - 20)
screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

# add to method





bird_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

bird = Bird()
bird_group.add(bird)

for i in range(4):
    ground = ArrierePlan(LARGEUR_SOL * i)
    ground_group.add(ground)
 
for i in range(4):
    pipes = arriere_plan.get_random_obstacle(LARGEUR_ECRAN * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

clock = pygame.time.Clock()

def main():
    global font, musique
    pygame.init()
    font = pygame.font.SysFont('Arial', 48)
    musique = Musique()
    while True:
        musique.jouerMusique()
        # ecran.blit(titre, titreRect)
        if jouer() == False:
            break
        pygame.display.update()
    
  
    pygame.display.set_caption('Happy Bird')
   

def gameoverText():
    global text, text2, textRect, text2Rect, oui, non, ouiRect, nonRect
    text = font.render('Game over', True, NOIR)
    text2 = font.render('Voulez-vous jouer encore?', True, NOIR)
    textRect = text.get_rect()
    textRect.center = (LARGEUR_ECRAN/2, HAUTEUR_ECRAN/2)

    text2 = font.render('Voulez-vous jouer encore?', True, NOIR)
    text2Rect = text2.get_rect()
    text2Rect.center = (int(LARGEUR_ECRAN / 2), int(HAUTEUR_ECRAN / 2) + 50)

    oui = font.render('Oui', True, NOIR)
    ouiRect = oui.get_rect()
    ouiRect.center = (int(LARGEUR_ECRAN / 2) - 60, int(HAUTEUR_ECRAN / 2) + 90)

    non = font.render('Non', True, NOIR)
    nonRect = non.get_rect()
    nonRect.center = (int(LARGEUR_ECRAN / 2) + 60, int(LARGEUR_ECRAN / 2) + 90)

def jouer():
    begin = True
    while begin:

        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.saut()
                    begin = False
        screen.blit(BACKGROUND, (0, 0))
    

        if arriere_plan.is_off_screen(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])

            new_ground = ArrierePlan(LARGEUR_SOL - 20)
            ground_group.add(new_ground)

        ground_group.update()

        bird_group.draw(screen)
        ground_group.draw(screen)

        pygame.display.update()

    running = True
    gameover = False
    while running:

        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.saut()

        screen.blit(BACKGROUND, (0, 0))

        if arriere_plan.is_off_screen(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])

            new_ground = ArrierePlan(LARGEUR_SOL - 20)
            ground_group.add(new_ground)

        if arriere_plan.is_off_screen(pipe_group.sprites()[0]):
            pipe_group.remove(pipe_group.sprites()[0])
            pipe_group.remove(pipe_group.sprites()[0])
            pipes = arriere_plan.get_random_obstacle(LARGEUR_ECRAN * 2)
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])


        bird_group.update()
        ground_group.update()
        pipe_group.update()
        bird_group.draw(screen)
        pipe_group.draw(screen)
        ground_group.draw(screen)

        if(gameover == False):
            pygame.display.update()

        if(gameover == False):
            if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                    pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
                    gameoverText()
                    print('Colision')
                    gameover = True

                    #ajouter une musique de fin
                    
                    screen.blit(text, (20,20))
                    screen.blit(text2, (20,60))
                    screen.blit(oui, (20,100))
                    screen.blit(non, (100,100))
                    # voulez vous continuer a jouer
                    pygame.display.flip()
        if(gameover == True):
            print('gameover')
            for event in pygame.event.get():
                        if event.type == MOUSEBUTTONUP:
                            xSouris, ySouris = event.pos
                            if ouiRect.collidepoint((xSouris, ySouris)):
                                print('oui')
                                begin = True
                            elif nonRect.collidepoint((xSouris, ySouris)):
                                print('non')
                                pygame.exit()

if __name__ == '__main__':
    main()
            
