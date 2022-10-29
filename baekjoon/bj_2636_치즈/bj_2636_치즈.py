from sys import stdin


def search_edges(R, C):
    edges = []

    for r in range(R):
        for c in range(C):
            if not r * c or (R - 1 == r or C - 1 == c):
                edges.append((r, c))
                visited[r][c] = 1

    return edges


def bfs_time(start):
    q = start

    while q:
        cr, cc = q.pop(0)

        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < R and 0 <= nc < C and visited[cr][cc] + cheeze[nr][nc] < visited[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + cheeze[nr][nc]
                q.append([nr, nc])


R, C = map(int, input().split()) # R: 행, C: 열
cheeze = [list(map(int, stdin.readline().rstrip().split())) for _ in range(R)]

visited = [[100*100]*C for _ in range(R)]
edges = search_edges(R, C)

bfs_time(edges)

cnt = [0] * (R*C+1)
last = -1

for r in range(R):
    for c in range(C):
        last = max(last, visited[r][c])

        if cheeze[r][c]:
            cnt[visited[r][c]] += 1

print(last-1)
print(cnt[last])
