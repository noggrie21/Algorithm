import sys
sys.stdin = open('2.txt')


def bfs(si, sj):
    q = [(si, sj)]
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    result = [(si, sj)]
    while q:
        i, j = q.pop(0)

        for di, dj in (0,1), (0,-1), (1,0), (-1,0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == arr[si][sj]:
                result.append((ni, nj))
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j]+1

    return result


def bfs2(q):
    visitied = [[0]*N for _ in range(N)]
    for i, j in q:
        visitied[i][j] = 1

    while q:

        i, j = q.pop(0)

        if arr[i][j] == 3:
            print(visitied)
            return visitied[i][j] - 1

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visitied[ni][nj]:
                q.append((ni, nj))
                visitied[ni][nj] = visitied[i][j] + 1

N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
q = bfs(0, 0)
print(bfs2(q))