from abc import ABC, abstractmethod

class Uninformed(ABC):
    def __init__(self):
        super().__init__()
        self.cell_path = dict 
        self.came_from = dict
        self.path = []
        self.visited = []
        self.informed = False

    @abstractmethod
    def search(self, grid_size, start, goals, obstacles):
        super().search(grid_size, start, goals, obstacles)
    
    # Backtracking the shortest path available
    def reconstruct_path_from_current_cell(self, cell_track, goal):
        current = goal
        path = []
        while current:
            path.append(current)
            current = cell_track[current]
        
        return path[::-1]
    
    def update_path(self, came_from, goal):
            map_direction = {(1,0): 'right', (-1,0): 'left', (0,1): 'down', (0,-1):'up'}
            current = goal
            path = []
            while current in came_from and came_from[current] is not None:
                path.append(came_from[current])
                for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    if map_direction[(dx, dy)] == came_from[current]:
                        current = (current[0] - dx, current[1] - dy)
                        break
            return path[::-1]

    # function map cell changes to directions and update path tracking dict    
    def get_direction(self, came_from, cell, dx, dy):
        map_direction = {(1,0): 'right', (-1,0): 'left', (0,1): 'down', (0,-1):'up'}
        came_from[cell] = map_direction[(dx,dy)]