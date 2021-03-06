def BFS(i, j):
    q = [(i, j)]
    paper[i][j] = 0

    width = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and paper[ni][nj]:
                q.append((ni, nj))
                paper[ni][nj] = 0
                width += 1

    return width


# 입력 받기
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

# 출력 변수
count_picture = width_picture = 0

# 그림 파악하기
for i in range(N):
    for j in range(M):
        if paper[i][j]:
            width_picture = max(BFS(i, j), width_picture)
            count_picture += 1

# 출력 하기
print(count_picture)
print(width_picture)
