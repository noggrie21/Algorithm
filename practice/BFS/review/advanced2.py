import sys
sys.stdin = open('ad2.txt')


def bfs1(si, sj):
    q = [(si, sj)]
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    result = [(si, sj)]
    while q:
        i, j = q.pop(0)

        for di, dj in (0,1), (0, -1), (1,0), (-1, 0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == arr[si][sj]:
                visited[ni][nj] = visited[i][j]+1
                q.append((ni, nj))
                result.append((ni, nj))

    return result


def bfs2(q):
    visited = [[0] * N for _ in range(N)]
    for i, j in q:
        visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return visited[i][j] -1
        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
q = bfs1(0,0)
print(bfs2(q))