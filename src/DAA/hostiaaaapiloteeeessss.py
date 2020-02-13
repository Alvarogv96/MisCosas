from _collections import deque


def dfs(grafo):
    cont = 0
    n = len(grafo)
    elementosvisitados = [False] * n
    for v in range(0, n):
        if not elementosvisitados[v]:
            cont = cont +1
            dfsrecursivo(grafo, elementosvisitados, v)
    return cont

def dfsrecursivo(grafo, elemetosvisitados, v):
    cola = deque()
    elemetosvisitados[v] = True
    #print(v, end=" ")
    cola.append(v)
    "Encolamos el elemento v"
    while cola:
        aux = cola.popleft()
        "Desencolamos por la izquierda"
        for adj in grafo[aux]:
            if not elemetosvisitados[adj]:
                elemetosvisitados[adj] = True
                #print(adj, end=" ")
                cola.append(adj)


grafo = []
#print("Introduce N y M: ")
N, M = list(map(int, input().split()))
for x in range(N):
    grafo.append([])
for y in range(M):
   # print("Introduzca pilote sin  patata: ")
    a, b = list(map(int, input().split()))
    grafo[a].append(b)
    grafo[b].append(a)
print(dfs(grafo))
