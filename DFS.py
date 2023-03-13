# Definición del grafo
grafo = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

# Función DFS
def dfs(grafo, nodo_inicial, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo_inicial)
    print(nodo_inicial)
    for vecino in grafo[nodo_inicial]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Ejecución del algoritmo DFS
dfs(grafo, 'A')
