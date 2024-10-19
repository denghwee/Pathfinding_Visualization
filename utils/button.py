import pygame
from utils.settings import *

class Button():
    def __init__(self, screen, height):
        self.screen = screen
        self.height = height

    def draw_buttons(self):
        #draw start button
        start_button = pygame.Rect(0, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "green", start_button)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Start', True, "white"), (20, self.height - 90))

        #draw stop button
        stop_button = pygame.Rect(300, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "red", stop_button)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Stop', True, "white"), (325, self.height - 90))

        #draw pause button
        pause_button = pygame.Rect(600, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "blue", pause_button)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Pause', True, "white"), (620, self.height - 90))

        #draw resume button
        resume_button = pygame.Rect(900, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "yellow", resume_button)
        self.screen.blit(pygame.font.Font(FONT, 24).render('Resume', True, "black"), (915, self.height - 90))

