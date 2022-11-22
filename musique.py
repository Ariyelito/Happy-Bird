import pygame


class Musique:
    def __init__(self):
        self.file = 'instrumental.mp3'

    def jouerMusique(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play(-1)
