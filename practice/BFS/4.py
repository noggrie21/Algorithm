import sys
sys.stdin = open('4.txt')


def BFS(si, sj):
    queue = [(si, sj)]
    visited[si][sj] = 1
    arr[si][sj] = 0
    while queue:
        i, j = queue.pop(0)

        for di, dj in (1, 0), (-1, 0), (0, -1), (0, 1):
            ni, nj = i + di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                arr[ni][nj] = 0
                queue.append((ni, nj))


N = 5

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt += 1
            BFS(i, j)

print(cnt)
print(visited)