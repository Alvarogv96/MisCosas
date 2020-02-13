def dfs(listadeadyacencia):
    n = len(listadeadyacencia)
    elementosvisitados = [False] * n
    "Array de elementos visitados de tamaño n"
    for v in range(1, n):
        "hay que señalar que empiece en 1 y no en 0"
        if not elementosvisitados[v]:
            dfsrecursiva(listadeadyacencia, elementosvisitados, v)


def dfsrecursiva(listadeadyacencia, elementosvisitados, v):
    "Marcamos como visitado el nodo "
    elementosvisitados[v] = True
    print(v, end=" ")
    "El end es para que no ponga por defecto un salto de linea sino un espacio en blanco"
    for adj in listadeadyacencia[v]:
        if not elementosvisitados[adj]:
            "en la primer interacion v =1 y adj = 2"
            dfsrecursiva(listadeadyacencia, elementosvisitados, adj)


listadeadyacencia = [[], [2, 4, 8], [1, 3, 4], [2, 4, 5], [1, 2, 3, 7], [3, 6], [5, 7], [4, 6, 9], [1, 9], [7, 8]]
"primera posicion seria 0 asi que la ponemos vacia para iniciar desde el 1"
dfs(listadeadyacencia)
