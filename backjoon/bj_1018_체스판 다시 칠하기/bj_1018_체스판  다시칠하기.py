def bfs(si, sj, types, ei, ej):
    global ans
    q = [0] * 64
    front = -1
    rear = 0
    q[rear] = (si, sj)
    visited = [[0]*M for _ in range(N)]
    visited[si][sj] = 1
    cnt = 0

    while front != rear:
        front += 1
        i, j = q[front]

        # visited가 홀수면서, types과 다를 때
        if visited[i][j] % 2 and board[i][j] ^ types:
            cnt += 1

        # visited가 짝수면서, types과 같을 때
        elif not visited[i][j] % 2 and not board[i][j] ^ types:
            cnt += 1

        for di, dj in (0, 1), (1, 0):
            ni, nj = i + di, j + dj
            if si <= ni < ei and sj <= nj < ej and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                rear += 1
                q[rear] = (ni, nj)

    ans = min(ans, cnt)


N, M = map(int, input().split()) # N:행 / M:열
board = [list(map(lambda x: (1 if x == 'W' else 0), input())) for _ in range(N)] # W: 1 / B: 0
ans = 64

for i in range(0, N-7):
    for j in range(0, M-7):
        bfs(i, j, 1, i+8, j+8)
        bfs(i, j, 0, i+8, j+8)
print(ans)