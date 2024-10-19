import pygame
from utils.GUI import Interface
from utils.settings import *

class Grid(Interface):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        super().__init__(grid_size, start, goals, obstacles, strategy)
        self.thick = CELLTHICK

    def draw_grid(self, screen):
        for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                color = self.determine_cell_color((i, j))
                pygame.draw.rect(screen, color, (i * (self.cell_size) + self.thick, j * (self.cell_size) + self.thick, self.cell_size - self.thick*2, self.cell_size - self.thick*2))
                
                if self.strategy.informed:
                    self.label_cell((i,j), screen)

    def determine_cell_color(self, cell):
        if cell == self.start:
            return 'red3'
        elif cell in self.goals:
            return 'springgreen4'
        elif cell in self.goals and self.strategy.informed:
            if cell == self.strategy.closest_goal:
                return 'green'
            else:
                return 'blue'
        elif cell in self.obstacles:
            return 'slategray4'
        else:
            return 'snow1'
        
    def informed_cell(self, cell, screen):
        x, y = cell
        heuristic_val = self.strategy.heuristic(cell, self.strategy.find_closest_goal(cell, self.goals))
        
        font = pygame.font.Font(None, 24)
        heuristic_text = font.render(f"h(n): {heuristic_val}", True, "black")
        screen.blit(heuristic_text, ((x + 0.3) * self.cell_size, (y + 0.1) * self.cell_size))
        
        if self.strategy.is_as and cell in self.strategy.g_score:
            g_score_text = font.render(f"g(n): {self.strategy.g_score[cell]}", True, "black")
            screen.blit(g_score_text, ((x + 0.3) * self.cell_size, (y + 0.8) * self.cell_size))