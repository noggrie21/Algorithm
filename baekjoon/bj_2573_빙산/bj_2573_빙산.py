def move_around(i, j):
    result = []

    for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
        ni, nj = di + i, dj + j

        if 0 <= ni < N and 0 <= nj < M:
            result.append([ni, nj])

    return result


def seperate_ice():
    melting_scores = [[0] * M for _ in range(N)]
    iceberg = []

    for i in range(N):
        for j in range(M):

            # 물인 경우
            if not arctic[i][j]:
                for ni, nj in move_around(i, j):
                        melting_scores[ni][nj] += 1

            # 빙산인 경우
            else:
                iceberg.append([i, j])

    return melting_scores, iceberg


def count_bundle(iceberg):
    if not iceberg:
        return 0

    q = [iceberg[0]]
    si, sj = q[0]
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        for ni, nj in move_around(ci, cj):
            if arctic[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append([ni, nj])

    for i, j in iceberg:
        if not visited[i][j]:
            return 2
    else:
         return 1


def after_a_year():
    remove = []

    for i, j in iceberg:
        arctic[i][j] = max(arctic[i][j]-melting_scores[i][j], 0)
        if not arctic[i][j]:
            remove.append([i, j])

    for i, j in remove:
        for ni, nj in move_around(i, j):
            melting_scores[ni][nj] += 1

        iceberg.remove([i, j])


# 입력받기
N, M = map(int, input().split())                                # N: 행 갯수, M: 열 갯수
arctic = [list(map(int, input().split())) for _ in range(N)]    # arctic: 초기 북극 (2차원 배열)

answer = 0

melting_scores, iceberg = seperate_ice()                        # melting_scores: 녹는 수치가 담긴 2차원 배열, iceberge: 빙산 좌표가 담기는 1차원 배열
cnt = count_bundle(iceberg)

while cnt == 1:                                                 # iceberg를 순회하며 몇 덩이로 구성되어 있는지 확인
    after_a_year()
    answer += 1
    cnt = count_bundle(iceberg)

if not cnt:
    answer = 0

print(answer)