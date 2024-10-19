import pygame
from utils.settings import *
from utils.button import Button
import sys

class Init():
    def __init__(self, grid_draw, event_handler):
        self.grid = grid_draw
        self.event = event_handler

        self.width = self.grid.grid_size[1] * self.grid.cell_size
        self.height = self.grid.grid_size[0] * self.grid.cell_size + 100
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.button = Button(self.screen, self.height)

        pygame.display.set_caption(CAPTION)

    def run(self):
        running = True
        self.screen.fill((0, 0, 0))
        while running:
            try:
                self.grid.draw_grid(self.screen)
                self.button.draw_buttons()
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.event.handle_mouse_event(event, self.height, self.screen)
            except:
                running = False

        pygame.quit()
        sys.exit()
