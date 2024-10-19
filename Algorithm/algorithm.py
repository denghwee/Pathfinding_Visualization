from queue import Queue
from Algorithm.uninformed_search import Uninformed
# from informed_search import Informed
from utils.settings import *

class DFS(Uninformed):
    def __init__(self):
        super().__init__()

    def search(self, grid_size, start, goals, obstacles):
        stack = [start]
        self.came_from = {start: None}
        self.cell_path = {start: None}
        cell_count = 0

        while stack:
            cell = stack.pop()

            if cell not in self.visited:
                self.visited.append(cell)
            if cell in goals:
                self.path = self.reconstruct_path_from_current_cell(self.cell_path, cell)
                return cell, cell_count, self.update_path(self.came_from, cell)
            
            for x, y in neighbours:
                neighbour = (cell[0] + x, cell[1] + y)
                if 0 <= neighbour[0] < grid_size[1] and 0 <= neighbour[1] < grid_size[0] and neighbour not in self.visited and neighbour not in obstacles:
                    self.get_direction(self.came_from, neighbour, x, y)
                    self.cell_path[neighbour] = cell
                    stack.append(neighbour)
                    self.visited.append(neighbour)
                    cell_count += 1

        return "No goal is reachable;", cell_count, None 


# class BFS(Informed):