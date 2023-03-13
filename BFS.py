# Definición del grafo
grafo = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

# Función BFS
def bfs(grafo, nodo_inicial, nodo_final):
    visitados = set()
    cola = [[nodo_inicial]]
    if nodo_inicial == nodo_final:
        return [nodo_inicial]
    while cola:
        ruta = cola.pop(0)
        nodo_actual = ruta[-1]
        if nodo_actual not in visitados:
            vecinos = grafo[nodo_actual]
            for vecino in vecinos:
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)
                if vecino == nodo_final:
                    return nueva_ruta
            visitados.add(nodo_actual)

# Ejecución del algoritmo BFS
ruta = bfs(grafo, 'A', 'F')
print(ruta)

