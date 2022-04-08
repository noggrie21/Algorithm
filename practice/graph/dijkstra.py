


V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    adjM[v1][v2] = w

print(adjM)

dijkstar(0, V)