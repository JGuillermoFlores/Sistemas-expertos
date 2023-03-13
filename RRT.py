import numpy as np
import matplotlib.pyplot as plt

class RRT:
    def __init__(self, start, goal, obstacles, x_limit, y_limit, step_size, max_iterations):
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.nodes = []

    def generate(self):
        self.nodes = [self.start]
        for i in range(self.max_iterations):
            x_rand = np.array([np.random.uniform(self.x_limit[0], self.x_limit[1]), np.random.uniform(self.y_limit[0], self.y_limit[1])])
            x_near = self.get_nearest_node(x_rand)
            x_new = self.extend(x_near, x_rand)
            if self.check_collision(x_near, x_new):
                self.nodes.append(x_new)
                if self.distance(x_new, self.goal) < self.step_size:
                    self.nodes.append(self.goal)
                    break
        path = self.get_path()
        return path

    def get_nearest_node(self, x_rand):
        distances = [self.distance(x_rand, x) for x in self.nodes]
        index_min = np.argmin(distances)
        return self.nodes[index_min]

    def extend(self, x_near, x_rand):
        dist = self.distance(x_near, x_rand)
        if dist <= self.step_size:
            return x_rand
        else:
            x_new = x_near + self.step_size * (x_rand - x_near) / dist
            return x_new

    def check_collision(self, x_near, x_new):
        for obstacle in self.obstacles:
            if obstacle.contains_point(x_new) or obstacle.intersects_line(x_near, x_new):
                return False
        return True

    def get_path(self):
        path = []
        x_last = self.nodes[-1]
        while not np.array_equal(x_last, self.start):
            for i in range(len(self.nodes)):
                if np.array_equal(self.nodes[i], x_last):
                    path.append(x_last)
                    x_last = self.nodes[i - 1]
                    break
        path.append(self.start)
        path.reverse()
        return path

    def distance(self, x1, x2):
        return np.linalg.norm(x1 - x2)

# Ejemplo de uso
from shapely.geometry import Polygon

# Definir los límites del espacio de trabajo
x_limit = [-5, 5]
y_limit = [-5, 5]

# Definir el punto de inicio y el punto objetivo
start = np.array([-4, -4])
goal = np.array([4, 4])

# Definir los obstáculos
obstacles = [
    Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
    Polygon([(2, 2), (3, 2), (3, 3), (2, 3)])
]

# Definir el tamaño de los pasos, el número máximo de iteraciones y crear el árbol RRT
step_size = 0.5
max_iterations = 1000
rrt = RRT(start, goal, obstacles, x_limit, y_limit, step_size, max_iterations)

# Generar el camino utilizando el árbol RRT
path = rrt.generate()

# Visualizar el resultado

