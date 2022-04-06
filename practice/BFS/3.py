

def bfs(si, sj):
    types = arr[si][sj]
    queue = [(si, sj)]
    visited[si][sj] = 1
    cnt = 0

    while queue:
        i, j = queue.pop(0)

        if arr[i][j] == types:
            cnt += 1

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == types:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))

    return cnt

N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
a = bfs(0, 0)
b = bfs(N-1, N-1)
print(a, b)