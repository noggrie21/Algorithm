import sys
sys.stdin = open('3.txt')


def bfs(si, sj):
    q = [(si, sj)]
    visited =[[0]*M for _ in range(N)]
    visited[si][sj] = 1

    while q:
        i, j = q.pop(0)

        if arr[i][j] == 3:
            return visited[i][j] - 1

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))



N = 5
M = 4
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(3, 1))