def bfs(si, sj):
    q = [(si, sj)]
    array[si][sj] = 0
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = ci + di, cj + dj
            if 0 < ni <= N and 0 < nj <= M and array[ni][nj]:
                cnt += 1
                q.append((ni, nj))
                array[ni][nj] = 0
    
    return cnt




N, M, K = map(int, input().split())

array = [[0] * (M+1) for _ in range(N+1)]
result = 0

for _ in range(K):
    r, c = map(int, input().split())
    array[r][c] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if array[i][j]:
            result = max(result, bfs(i, j))

print(result)
