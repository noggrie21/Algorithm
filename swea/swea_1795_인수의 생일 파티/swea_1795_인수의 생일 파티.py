import sys
sys.stdin = open('input (1).txt', 'r')
# sys.stdout = open('print.txt', 'w')

T = int(input())


def dijkstra(s):
    global tc
    dist = [0] + [initial] * N
    visited = [1] + [0] * N
    dist[s] = 0
    visited[s] = 1

    idx = -1
    minV = initial

    for i in range(1, N+1):
        if adjM[s][i] and adjM[s][i] < dist[i]:
            dist[i] = adjM[s][i]
            if minV > adjM[s][i]:
                minV = adjM[s][i]
                idx = i

    visited[idx] = 1

    for _ in range(N-2):
        for j in range(1, N+1):
            if not visited[j] and dist[j] > dist[idx] + adjM[idx][j]:
                idx = j
                dist[j] = dist[idx] + adjM[idx][j]
        visited[idx] = 1

        if tc == 1 or tc == 2:
            print(s, i, idx)
            print(adjM)
            print(dist)
            print(visited)
            print('-----')



for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    initial = N * 100
    adjM = [[0]*(N+1) for _ in range(N+1)]
    # print(N, M, X, graph)

    for _ in range(M):
        x, y, c = map(int, input().split())
        adjM[x][y] = c

    dijkstra(X)
