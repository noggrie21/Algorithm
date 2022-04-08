def BFS(si, sj, end):
    queue = [(si, sj)]
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1

    while queue:
        i, j = queue.pop(0)

        if arr[i][j] == end:
            print(visited)
            return visited[i][j] - 1

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


N = 4
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
cnt += BFS(0, 0, 3)
cnt += BFS(N-1, N-1, 4)

print(cnt)