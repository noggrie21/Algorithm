from collections import deque

monky_type, horse_type = 0, 1

monky = [(0, 1, monky_type), (0, -1, monky_type), (1, 0, monky_type), (-1, 0, monky_type)]

horse = [(1, -2, horse_type), (-2, -1, horse_type), (2, -1, horse_type),
         (-1, 2, horse_type), (-1, -2, horse_type), (-2, 1, horse_type),
         (2, 1, horse_type), (1, 2, horse_type)]


def bfs():
    maxC = 200*200
    q = deque()
    q.append((0,  0, K))
    # print(q)
    visited = [[[maxC, K] for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 0
    answer = maxC

    while q:
        cy, cx, k = q.popleft()
        for dy, dx, type in monky + horse * bool(k):
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < H and 0 <= nx < W and not zoo[ny][nx] and (visited[cy][cx][0] + 1 < visited[ny][nx][0] or visited[ny][nx][1] < (k - bool(type))):
                # print(f'cy: {cy} | cx: {cx} | ny: {ny} | nx: {nx} | k: {k}')
                visited[ny][nx] = [visited[cy][cx][0] + 1, k - bool(type)]
                # print(f'visited[cy][cx]: {visited[cy][cx]} | visited[ny][nx]: {visited[ny][nx]}  ')
                q.append((ny, nx, k - bool(type)))

                if ny == H-1 and nx == W-1:
                    answer = min(answer, visited[ny][nx][0])

    if answer == maxC:
        return -1
    return answer


K = int(input())
W, H = map(int, input().split())
zoo = [list(map(int, input().split())) for _ in range(H)]

if W == H == 1:
    print(0)
else:
    answer = bfs()
    print(answer)
