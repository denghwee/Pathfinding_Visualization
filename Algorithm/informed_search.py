from abc import abstractmethod
from Algorithm.uninformed_search import Uninformed

class Informed(Uninformed):
    def __init__(self):
        super().__init__()
        self.informed = True
        self.closest_goal = tuple

    @abstractmethod  
    def search(self, grid_size, start, goals, obstacles):
        pass

    def find_closest_goal(self, cell, goals):
        self.closest_goal = goals[0]

        for i in range(len(goals)):
            if self.heuristic(cell, goals[i]) < self.heuristic(cell, self.closest_goal):
                self.closest_goal = goals[i]

        return self.closest_goal
    
    def heuristic(self, cell, goal):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])