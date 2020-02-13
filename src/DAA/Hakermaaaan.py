def sumavalor(grafo, costes):
    valor = 0
    for x in range(len(grafo)):
        if len(grafo[x]) > 1:
            valor = valor + costes[x]
    return valor


grafo = []
# print("Introduce N y M: ")
N, M = list(map(int, input().split()))
for x in range(N):
    grafo.append([])
costes = []
for j in range(N):
    c = int(input())
    costes.append(c)

for y in range(M):
    # print("Introduzca pilote sin  patata: ")
    a, b = list(map(int, input().split()))
    grafo[a].append(b)
    grafo[b].append(a)
# print(costes)
# print(grafo)
print(sumavalor(grafo, costes))
