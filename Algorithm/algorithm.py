from queue import Queue
from Algorithm.uninformed_search import Uninformed
from Algorithm.informed_search import Informed
from heapq import heappush, heappop
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
                return cell, cell_count, self.reconstruct_path_from_current_cell(self.came_from, cell)
            
            for x, y in neighbours:
                neighbour = (cell[0] + x, cell[1] + y)
                if 0 <= neighbour[0] < grid_size[1] and 0 <= neighbour[1] < grid_size[0] and neighbour not in self.visited and neighbour not in obstacles:
                    self.get_direction(self.came_from, neighbour, x, y)
                    self.cell_path[neighbour] = cell
                    stack.append(neighbour)
                    self.visited.append(neighbour)
                    cell_count += 1

        return "No attainable path!", cell_count, None
    
class BFS(Uninformed):
    def __init__(self):
        super().__init__()

    def search(self, grid_size, start, goals, obstacles):
        q = Queue()
        q.put(start)

        self.came_from = {start: None}
        self.cell_path = {start: None}
        self.visited.append(start)
        cell_count = 0
        
        while not q.empty():
            cell = q.get()

            if cell in goals:
                self.path = self.reconstruct_path_from_current_cell(self.cell_path, cell)
                return cell, cell_count, self.update_path(self.came_from, cell)


            for x,y in neighbours:
                neighbour = (cell[0] + x, cell[1] + y)
                if 0 <= neighbour[0] < grid_size[1] and 0 <= neighbour[1] < grid_size[0] and neighbour not in self.visited and neighbour not in obstacles:
                    self.get_direction(self.came_from, neighbour, x, y)
                    self.visited.append(neighbour)
                    self.cell_path[neighbour] = cell
                    q.put(neighbour)
                    cell_count += 1
                    
        return "No attainable path!", cell_count, None      

class AS(Informed):
    def __init__(self):
        super().__init__()
        self.g_score = {tuple: 0}
        self.is_as = True

    def search(self, grid_size, start, goals, obstacles):
        open_set = [(self.heuristic(start, self.find_closest_goal(start, goals)), start)]
        self.came_from = {start: None}
        self.cell_path = {start: None}
        self.g_score = {start: 0}

        cell_count = 0

        while open_set:
            heuristic_val, current = heappop(open_set)

            if current in goals:
                self.path = self.reconstruct_path_from_current_cell(self.cell_path, current)
                return current, cell_count, self.update_path(self.came_from, current)

            for x, y in neighbours:
                neighbour = (current[0] + x, current[1] + y)
                tentative_g_score = self.g_score[current] + 1
                closest_goal = self.find_closest_goal(neighbour, goals)
                if 0 <= neighbour[0] < grid_size[1] and 0 <= neighbour[1] < grid_size[0] and neighbour not in self.visited and neighbour not in obstacles and tentative_g_score + self.heuristic(neighbour, closest_goal) < self.g_score.get(neighbour, float("inf")) + heuristic_val:
                        self.get_direction(self.came_from, neighbour, x, y)
                        self.visited.append(neighbour)
                        self.g_score[neighbour] = tentative_g_score
                        self.cell_path[neighbour] = current
                        heappush(open_set, (tentative_g_score + self.heuristic(neighbour, closest_goal), neighbour))
                        cell_count += 1

        return "No attainable path!", cell_count, None 
    