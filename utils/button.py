import pygame
from utils.settings import *

class Button():
    def __init__(self, screen, height):
        self.screen = screen
        self.height = height

    def draw_buttons(self):
        #draw start button
        start_button = pygame.Rect(50, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "forestgreen", start_button, border_radius=20)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Start', True, "white"), (70, self.height - 90))

        #draw stop button
        stop_button = pygame.Rect(350, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "firebrick", stop_button, border_radius=20)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Stop', True, "white"), (375, self.height - 90))

        #draw pause button
        pause_button = pygame.Rect(650, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "dodgerblue4", pause_button, border_radius=20)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Pause', True, "white"), (670, self.height - 90))

        #draw resume button
        resume_button = pygame.Rect(950, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "gold", resume_button, border_radius=20)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Resume', True, "black"), (965, self.height - 90))

