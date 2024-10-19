from utils.settings import *

class Agent():
    def __init__(self, strategy):
        self.strategy = strategy

    def perform_search(self, grid_size, start, goals, obstacles):
        return self.strategy.search(grid_size, start, goals, obstacles)