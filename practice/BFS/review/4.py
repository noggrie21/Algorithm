import sys
sys.stdin = open('4.txt')


def bfs(si, sj):
    q = [(si, sj)]
    visited = [[-1]*N for _ in range(N)]
    visited[si][sj] = 2

    while q:
        i, j = q.pop(0)

        for di, dj in (0, 1), (0, -1), (1, 0), (-1,0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
bfs(0, 0)