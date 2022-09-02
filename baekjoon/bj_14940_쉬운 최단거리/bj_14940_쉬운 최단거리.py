def search_start():
    start = []

    for i in range(1, N+1):
        for j in range(1, M+1):

            if arr[i][j] == 2:
                start = [i, j]

            elif not arr[i][j]:
                visited[i][j] = 0

    return start


def BFS(start):
    i, j = start
    q = [[i, j]]
    visited[i][j] = 0

    while q:
        # queue에서 맨 앞 원소 하나 빼기
        ci, cj = q.pop(0)

        # queue에 넣기
        for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
            ni, nj = ci + di, cj + dj

            if arr[ni][nj] and visited[ci][cj] + 1 < visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1


N, M = map(int, input().split())  # N: 행 크기, M = 열 크기
arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]

maxV = 1000 * 1000
visited = [[maxV] * (M+2) for _ in range(N+2)]

start = search_start()
BFS(start)

for lst in visited[1:N+1]:
    if maxV in lst:
        lst = list(map(lambda x: -1 if x == maxV else x, lst))
    print(*lst[1:M+1])
