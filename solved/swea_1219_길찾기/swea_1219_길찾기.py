import sys
sys.stdin = open('input (1).txt')


def dfs(v):
    global visited
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for j in range(100):
                if G[v][j] == 1 and not visited[j]:
                    stack.append(j)
    if visited[99]: return 1
    else: return 0


for a in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0] * 100 for _ in range(100)]
    visited = [0] * 100
    for i in range(E):
        G[temp[i*2]][temp[i*2+1]] = 1
    result = dfs(0)
    print(f'#{tc} {dfs(0)}')


