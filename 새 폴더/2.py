
maps = ["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]

print(ord('.'))
print(ord('A'))

def bfs(r, c):
    alphabet = [0] * 27
    q = [[r, c]]
    visited[r][c] = 1
    alphabet[array[r][c]] += 1

    while q:
        # 큐에서 빼기
        cr, cc = q.pop(0)

        # 큐에 넣기
        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            nr, nc = dr + cr, dc + cc
            if 0 <= nr < R and 0 <= nc < C:
                if array[nr][nc] and not visited[nr][nc]:
                    alphabet[array[r][c]] += 1
                    q.append([nr, nc])
                    visited[nr][nc] += visited[cr][cc]


    big = max(alphabet)
    country = []
    loser = 0
    for i in range(26, 0, -1):
        if big == alphabet[i]:
            country.append(i)
        else:
            loser += alphabet[i]
            alphabet[i] = 0

    alphabet[max(country)] += loser
    return alphabet


array = []
for temp in maps:
    array.append(list(map(lambda x: ord(x)-ord('A') + 1 if ord(x) > ord('.') else 0, temp)))

R = len(maps)
C = len(maps[0])


visited = [[0] * C for _ in range(R)]
print(visited)
status = [0] * 27

for r in range(R):
    for c in range(C):
        if array[r][c] and not visited[r][c]:
            result = bfs(r, c)
            for i in range(1, 27):
                status[i] += result[i]

answer = max(status)
print(answer)