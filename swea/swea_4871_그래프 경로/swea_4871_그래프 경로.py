import sys
sys.stdin = open('sample_input.txt')


def dfs(v):
    global visited
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for j in range(1, V+1):
                if G[v][j] == 1 and not visited[j]:
                    stack.append(j)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # print(f'#{tc} {V} {E}') #1 6 5 > #2 7 4 > #3 9 9
    visited = [0] * (V + 1)
    G = [[0] * (V + 1) for _ in range(V + 1)]
    for e in range(E):
        x, y = map(int, input().split())
        G[x][y] = 1
    start, end = map(int, input().split())
    dfs(start)
    print(f'#{tc} {visited[end]}')

