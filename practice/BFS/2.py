import sys
sys.stdin = open('2.txt')

def bfs(start):
    queue = start
    visited = [[0]*N for _ in range(N)]
    visited[start[0][0]][start[0][1]] = 1

    while queue:
        i, j = queue.pop(0)

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < N  and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj]=visited[i][j] + 1
                queue.append((ni, nj))

    print(visited)




N = 4
arr = [list(map(int, input().split())) for _ in range(N)]
start = [(0, 3), (1, 1), (3, 3)]
bfs(start)