def BFS(i, j):
    q = [(i, j)]
    arr[i][j] = 1
    empty = 1

    while q:
        # q에서 제거하기
        ci, cj = q.pop(0)

        # q에 삽입하기
        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N and not arr[ni][nj]:
                empty += 1
                q.append((ni, nj))
                arr[ni][nj] = 1

    return empty


def divide(arr):
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())

        for i in range(y1, y2):
            for j in range(x1, x2):
                arr[i][j] = 1

    return arr


def count_empty(cnt, areas):
    for i in range(M):
        for j in range(N):
            if not arr[i][j]:
                cnt += 1
                areas.append(BFS(i, j))
    return cnt, areas


# 입력받기
M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]

# 좌표 반영하여, 영역 구분하기
arr = divide(arr)

# 빈 영역 카운트하기
cnt, areas = count_empty(0, [])

# 출력하기
print(cnt)
print(*sorted(areas))