# -*- coding: utf-8 -*-
from queue import PriorityQueue

class BestFirstSearch:
    def __init__(self, start, goal, get_neighbors, heuristic):
        self.start = start
        self.goal = goal
        self.get_neighbors = get_neighbors
        self.heuristic = heuristic

    def search(self):
        queue = PriorityQueue()
        queue.put((self.heuristic(self.start, self.goal), self.start))
        visited = set()
        while not queue.empty():
            _, current = queue.get()
            if current == self.goal:
                return self.get_path(current)
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    queue.put((self.heuristic(neighbor, self.goal), neighbor))
        return None

    def get_path(self, current):
        path = []
        while current is not None:
            path.append(current)
            current = current.parent
        return list(reversed(path))

# Ejemplo de uso
import numpy as np

# Definir el estado inicial y el estado objetivo
start = (0, 0)
goal = (5, 5)

# Definir una función para obtener los vecinos de un estado
def get_neighbors(state):
    x, y = state
    neighbors = []
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + i, y + j
        if 0 <= new_x <= 5 and 0 <= new_y <= 5:
            neighbors.append((new_x, new_y))
    return neighbors

# Definir una función heurística (distancia euclidiana)
def heuristic(state, goal):
    x1, y1 = state
    x2, y2 = goal
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Crear una instancia de BestFirstSearch y realizar la búsqueda
bfs = BestFirstSearch(start, goal, get_neighbors, heuristic)
path = bfs.search()

# Imprimir el resultado
if path:
    print(f"El camino encontrado es: {path}")
else:
    print("No se encontró camino")
