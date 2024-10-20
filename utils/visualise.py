from utils.GUI import Interface
from utils.settings import *
import pygame

class Visualise(Interface):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        super().__init__(grid_size, start, goals, obstacles, strategy)
        self.thick = 2


    def visualise_search(self, cell, screen):
        x, y = cell
        color = 'red' if cell == self.start else 'gold1'

        pygame.draw.rect(screen, color, (x * (self.cell_size) + self.thick, y * (self.cell_size) + self.thick, self.cell_size - self.thick*2, self.cell_size - self.thick*2), border_radius=5)
        
        if self.strategy.informed:
            self.label_cell(cell, screen)
            

    def label_cell(self, cell, screen):
        x, y = cell
        heuristic_val = self.strategy.heuristic(cell, self.strategy.find_closest_goal(cell, self.goals))
        
        font = pygame.font.Font(FONT, 12)
        heuristic_text = font.render(f"h(n): {heuristic_val}", True, "black")
        screen.blit(heuristic_text, ((x + 0.3) * self.cell_size, (y + 0.1) * self.cell_size))
        
        if self.strategy.is_as and cell in self.strategy.g_score:
            g_score_text = font.render(f"g(n): {self.strategy.g_score[cell]}", True, "black")
            screen.blit(g_score_text, ((x + 0.3) * self.cell_size, (y + 0.8) * self.cell_size))


    def highlight_final_path(self, screen):
        path = self.strategy.path
        for cell in path:
            x, y = cell
            pygame.draw.rect(screen, 'chocolate1', (x * (self.cell_size) + self.thick, y * (self.cell_size) + self.thick, self.cell_size - self.thick*2, self.cell_size - self.thick*2), border_radius=5)  # Orange color for the path
        
        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.quit()