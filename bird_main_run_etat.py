import pygame
from background import *
from bird import *
from obstacle import *
from musique import *

#VARIABLES
SCREEN_WIDHT = 640
SCREEN_HEIGHT = 480
SPEED = 20
GRAVITY = 2.5
GAME_SPEED = 15

GROUND_WIDHT = 2 * SCREEN_WIDHT
 

PIPE_WIDHT = 80
PIPE_HEIGHT = 500

PIPE_GAP = 150

arriere_plan = ArrierePlan(GROUND_WIDHT - 20)
 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

BACKGROUND = pygame.image.load('img/background/flappy_bird_bg3.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDHT, SCREEN_HEIGHT))
#BEGIN_IMAGE = pygame.image.load('assets/sprites/message.png').convert_alpha()

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()

for i in range (2):
    ground = ArrierePlan(GROUND_WIDHT * i)
    ground_group.add(ground)

pipe_group = pygame.sprite.Group()

for i in range (2):
    pipes = arriere_plan.get_random_pipes(SCREEN_WIDHT * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

clock = pygame.time.Clock()

begin = True

while begin:

    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird.bump()
                pygame.mixer.music.load('instrumental.mp3')
                pygame.mixer.music.play()
                begin = False

    screen.blit(BACKGROUND, (0, 0))

    if arriere_plan.is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = ArrierePlan(GROUND_WIDHT - 20)
        ground_group.add(new_ground)

    bird.begin()
    ground_group.update()

    bird_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update()


while True:

    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird.bump() 
                pygame.mixer.music.load('instrumental.mp3')
                pygame.mixer.music.play()

    screen.blit(BACKGROUND, (0, 0))

    if arriere_plan.is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = ArrierePlan(GROUND_WIDHT - 20)
        ground_group.add(new_ground)

    if arriere_plan.is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])

        pipes = arriere_plan.get_random_pipes(SCREEN_WIDHT * 2)

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
        pygame.mixer.music.load('instrumental.mp3')
        pygame.mixer.music.play()
        break