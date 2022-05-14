T = int(input())


def bfs(r, c):
    q = [(r, c)]
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1

    while q:
        cr, cc = q.pop()
        field[cr][cc] = 0

        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and field[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return 1


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    ans = 0

    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1

    for r in range(N):
        for c in range(M):
            if field[r][c]:
                ans += 1
                field[r][c] = 0
                while
                for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and field[nr][nc]:
                        field[nr][nc] = 0

    print(ans)