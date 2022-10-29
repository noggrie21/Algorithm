def bfs(si, sj, start):
    q = [(si, sj)]
    visited[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and war[ni][nj] == start and not visited[ni][nj]:
                q.append((ni, nj))
                cnt += 1
                visited[ni][nj] = 1

    return cnt ** 2


N, M = map(int, input().split())

war = [list(map(lambda x:0 if x == 'W' else 1, input())) for _ in range(N)]
result = [0, 0]  # [0]: 아군, [1]: 적군

visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result[war[i][j]] += bfs(i, j, war[i][j])

print(*result)