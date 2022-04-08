# 4. 벽 부수기

import sys
sys.stdin = open('8.txt')


def bfs(sr, sc):
    q = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 2

    while q:
        r, c = q.pop(0)

        for dr, dc in (0,1), (0, -1), (1, 0), (-1, 0):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                # 새로운 칸이 벽이 아닐 떄,
                if not arr[nr][nc] and vi

                # 새로운 칸이 벽일 때,
                if  arr[nr][nc] == 1 and 1 <= visited[r][c]:




N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
bfs(0, 0)