def bfs(si, sj, types):
    global ans
    q = [0] * 64
    arr = [[0] * M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    front = -1
    rear = 0
    q[rear] = (si, sj)
    visited[si][sj] = 1

    while front != rear:
        front += 1
        i, j = q[front]

        # visited가 홀수면서, types과 다를 때
        if visited[i][j] % 2 and board[i][j] ^ types:
            arr[i][j] = 1

        # visited가 짝수면서, types과 같을 때
        elif not visited[i][j] % 2 and not board[i][j] ^ types:
            arr[i][j] = 1

        for di, dj in (0, 1), (1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                rear += 1
                q[rear] = (ni, nj)

    return arr


def count_diff(arr):
    ans = N*M
    for i in range(0, N-7):
        for j in range(0, M-7):
    return ans

N, M = map(int, input().split()) # N:행 / M:열
board = [list(map(lambda x: (1 if x == 'W' else 0), input())) for _ in range(N)] # W: 1 / B: 0
ans = 64
type_zero = bfs(0, 0, 0)
type_one = bfs(0, 0, 1)
print(min(count_diff(type_zero), count_diff(type_one)))
# for i in range(0, N-7):
#     for j in range(0, M-7):
#         bfs(i, j, 1, i+8, j+8)
#         bfs(i, j, 0, i+8, j+8)
# print(ans)