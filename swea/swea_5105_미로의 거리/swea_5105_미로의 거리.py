import sys
sys.stdin = open('sample_input.txt')


def find(miro, N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if miro[i][j] == 2:
                return i, j


def bfs(i, j, N):
    queue = [(i, j)]
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        if miro[i][j] == 3:
            return visited[i][j] - 2
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if miro[ni][nj] != 1 and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


def dfs(i, j, N, c):
    global minV
    if miro[i][j] == 3:
        if minV > 3:
            minV = c
    else:
        miro[i][j] = 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if miro[ni][nj] != 1:
                dfs(ni, nj, N, c + 1)
        miro[i][j] = 0


T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N = int(input())
    miro = [[1] * (N + 2)] +[[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    i, j = find(miro, N)
    # result = bfs(i, j, N)
    # print(f'#{tc} {result}')
    minV = 100 * 100
    dfs(i, j, N, 0)
    if minV == 10000:
        minV = 1
    print(f'#{tc} {minV-1}')
    # visited = [0] * (N + 1)
    # queue = [v]
    # while queue:
    #     i, j = queue.pop(0)
    #     if not visited[i][j]:
    #         visited[i][j] = 1
    #         if G[i][j] == 3:
    #             break
    #         for i in G[]

