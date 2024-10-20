from utils.GUI import Interface
from utils.visualise import Visualise
import pygame


class Event(Interface):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        super().__init__(grid_size, start, goals, obstacles, strategy)
        self.active = False
        self.paused = False
        self.visual = Visualise(grid_size, start, goals, obstacles, strategy)

    def handle_mouse_event(self, event, height, screen):
        x, y = event.pos
        if (60 <= x <= 140 and height - 90 <= y <= height - 60):
            self.start_search(height, screen)

    def start_search(self, height, screen):
        if not self.active:
            self.active = True
            self.paused = False

            for cell in self.strategy.visited:
                if not self.active:
                    break

                while self.paused:
                    self.wait_until_resumed(height)

                self.handle_events(height)
                self.visual.visualise_search(cell, screen)
                pygame.display.flip()
                pygame.time.delay(500)

            if self.active:
                self.visual.highlight_final_path(screen)

    def handle_events(self, height):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 360 <= x <= 440 and height - 90 <= y <= height - 60:
                    self.active = False
                elif 660 <= x <= 740 and height - 90 <= y <= height - 60:
                    self.paused = True


    def wait_until_resumed(self, height):
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 960 <= x <= 1040 and height - 90 <= y <= height - 60:
                        self.paused = False
                    if 360 <= x <= 440 and height - 90 <= y <= height - 60:
                        self.active = False 
                        self.paused = False