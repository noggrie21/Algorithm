def bfs(sr, sc):
    q = [(sr, sc)]
    visited = [[0]*(M+1) for _ in range(N+1)]
    visited[sr][sc] = 1

    while q:
        cr, cc = q.pop(0)

        if cr == N and cc == M:
            return visited[cr][cc]

        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr, nc = cr+dr, cc+dc
            if 0 <= nr <= N and 0 <= nc <= M and arr[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[cr][cc] + 1


from sys import stdin
N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0] + list(map(int, stdin.readline().rstrip())) for _ in range(N)]
print(bfs(1, 1))