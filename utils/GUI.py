from abc import ABC
from utils.settings import *
import pygame
import os

class Interface(ABC):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        pygame.init()

        self.grid_size = grid_size
        self.start = start
        self.goals = goals
        self.obstacles = obstacles
        self.strategy = strategy
        self.cell_size = CELLSIZE