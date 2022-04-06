import sys
sys.stdin = open('5.txt')



def BFS(si, sj):
    queue = [(si, sj)]
    visited[si][sj] = 1

    while queue:
        i, j = queue.pop(0)
        print(i, j, arr[i][j])
        if arr[i][j] == 3:
            print(i, j)
            print(visited[i][j])
            return visited[i][j] - 1

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 1:
                # print(ni, nj)
                visited[ni][nj] = visited[i][j] + 1
                queue.append((si, nj))





N = 5
M = 4
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
print(visited)
print(BFS(0, 0))
print(visited)
