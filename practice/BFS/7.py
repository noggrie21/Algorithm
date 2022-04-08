import sys
sys.stdin = open('7.txt')


def BFS(si, sj):
    q = [(si, sj)]
    visited = [[0]*M for _ in range(N)]
    visited[si][sj] = 1

    while q:
        i, j = q.pop(0)
        if arr[i][j] == 2:
            print(visited)
            return visited[i][j] - 1

        for di, dj in [(0,1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))


N, M = 6, 4

arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 3:
            ans = BFS(i, j)
print(ans)
