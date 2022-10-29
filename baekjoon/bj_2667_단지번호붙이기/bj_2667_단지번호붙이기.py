def bfs(r, c):
    q = [(r, c)]
    visited[r][c] = 1
    maps[r][c] = 0
    cnt = 1

    while q:
        cr, cc = q.pop(0)

        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            nr = dr + cr
            nc = dc + cc
            if maps[nr][nc]:
                cnt += 1
                maps[nr][nc] = 0
                q.append((nr, nc))

    return cnt


N = int(input())
maps = [[0] * (N+2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] + [[0] * (N+2)]

answer = [0]
n = 1
visited = [[0] * (N+2) for _ in range(N+2)]

for r in range(1, N+1):
    for c in range(1, N+1):
        if maps[r][c]:
            answer.append(bfs(r, c,))
            n += 1

print(n-1)
answer.sort()
for i in range(1, n):
    print(answer[i])