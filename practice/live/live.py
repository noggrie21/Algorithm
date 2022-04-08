def BFS(start):
    queue = start

    while queue:
        i, j = queue.pop(0)

        for di, dj in (0,1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))

    print(visited)

N = 4
arr = [[0] * N for _ in range(N)]
start = [(1,1), (0,3), (3, 3)]
visited = [[0] * N for _ in range(N)]
for si, sj in start:
    arr[si][sj] = 1
    visited[si][sj] = 1
BFS(start)
print(arr)

arr = [[]]