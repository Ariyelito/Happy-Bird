'''
Explication du scroll ici
https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame
'''
import pygame

class ArrierePlan:
    def __init__(self, largeur, hauteur):
        self.image = pygame.image.load('img/background/flappy_bird_bg3.png')
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.largeur = largeur
        self.hauteur = hauteur
        self.pos_x = 0
        self.pos_y = 0
        self.vitesse_x = 1

    def dessiner(self, screen):
        screen.blit(self.image, (self.pos_x,0))
        screen.blit(self.image, (self.pos_x + self.largeur,0))

        self.pos_x -= self.vitesse_x
        if self.pos_x <= -self.largeur:
            self.pos_x = 0


def test():
    print("Test")
    pygame.init()

    FPS = 60 # frames per second setting
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Flappy Bird made by Ricardo!")

    arriere_plan = ArrierePlan(640, 480)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        arriere_plan.dessiner(screen)

        pygame.display.update()
        fpsClock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    test()

