from _collections import deque


def dfs(grafo):
    n = len(grafo)
    elementosvisitados = [False] * n
    for v in range(1, n):
        if not elementosvisitados[v]:
            dfsrecursivo(grafo, elementosvisitados, v)


def dfsrecursivo(grafo, elemetosvisitados, v):
    cola = deque()
    elemetosvisitados[v] = True
    print(v, end=" ")
    cola.append(v)
    "Encolamos el elemento v"
    while cola:
        aux = cola.popleft()
        "Desencolamos por la izquierda"
        for adj in grafo[aux]:
            if not elemetosvisitados[adj]:
                elemetosvisitados[adj] = True
                print(adj, end=" ")
                cola.append(adj)


"""grafo = [[], [2, 4, 8], [1, 3, 4], [2, 4, 5], [1, 2, 3, 7], [3, 6], [5, 7], [4, 6, 9], [1, 9], [7, 8]]
bfs(grafo)"""
grafo = []
print("Introduzca el numero de nodos")
nodos = int(input())
for x in range(nodos):
    print("introduzca adyacentes del no ", x, " :")
    m = list(map(int, input().split()))
    grafo.append(m)
    print(grafo)
dfs(grafo)
