from Algorithm.algorithm import *
from utils.grid import Grid
from utils.agent import Agent
from utils.init import load_file
from utils.event import Event
from initiator import Init

import sys

def main(filename, method):
    try:
        grid, start, goal, obstacles = load_file(filename)
    except:
        print('File\'s format or dir error!')

    if method.lower() == 'dfs':
        strategy = DFS()
    elif method.lower() == 'bfs':
        strategy = BFS()
    elif method.lower() == 'as':
        strategy = AS()
    else:
        print('Invalid pathfinding method. Please use the available algorithms, such as: \'bfs\', \'dfs\'.')
        return

    agent = Agent(strategy)
    try:
        cell, cell_count, path = agent.perform_search(grid, start, goal, obstacles)
    except:
        return

    # print the outputs on the terminal
    print(filename, method)
    print(cell, cell_count)
    if path is not None:
        print(path)

    # set up GUI
    event = Event(grid, start, goal, obstacles, strategy)
    grid = Grid(grid, start, goal, obstacles, strategy)
    GUI_instance = Init(grid, event)
    GUI_instance.run()
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python search.py <filename> <method>')
    else:
        main(sys.argv[1], sys.argv[2])