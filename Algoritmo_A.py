import heapq

# Definir las funciones necesarias para el algoritmo A*
def a_estrella(mapa, inicio, objetivo):
    frontera = []
    heapq.heappush(frontera, (0, inicio))
    costo_actual = {inicio: 0}
    padre = {inicio: None}

    while frontera:
        _, actual = heapq.heappop(frontera)

        if actual == objetivo:
            # Se ha llegado al objetivo, se reconstruye el camino desde el inicio
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            return camino[::-1]

        # Se exploran los vecinos del nodo actual
        for vecino in obtener_vecinos(actual, mapa):
            nuevo_costo = costo_actual[actual] + 1

            if vecino not in costo_actual or nuevo_costo < costo_actual[vecino]:
                costo_actual[vecino] = nuevo_costo
                prioridad = nuevo_costo + distancia_manhattan(vecino, objetivo)
                heapq.heappush(frontera, (prioridad, vecino))
                padre[vecino] = actual

    return None

def obtener_vecinos(nodo, mapa):
    vecinos = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x = nodo[0] + dx
        y = nodo[1] + dy
        if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] == 0:
            vecinos.append((x, y))
    return vecinos

def distancia_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Definir el mapa como una matriz de 0 y 1, donde 0 es un espacio libre y 1 es un obstáculo
mapa = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Definir las posiciones de inicio y objetivo en el mapa
inicio = (0, 0)
objetivo = (4, 4)

# Utilizar el algoritmo A* para encontrar el camino más corto entre el inicio y el objetivo en el mapa
camino = a_estrella(mapa, inicio, objetivo)

# Imprimir el camino encontrado
print(camino)
