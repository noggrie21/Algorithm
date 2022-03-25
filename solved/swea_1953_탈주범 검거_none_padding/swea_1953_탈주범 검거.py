import sys
sys.stdin = open('sample_input.txt')
# 출력 : 탈주범이 위치할 수 있는 장소의 개수
# 탈주범은 1시간에 1거리 이동
# 지하터널의 크기 세로 N, 가로 M (5 <= N, M <= 50)
# 맨홀 뚜껑 (R, C)
# 소요시간 : L (1 <= L <= 20)
# L = 1일때, 탈주범위 위치 = (R , C)
# 지하 터널 지도에는 반드시 1개 이상의 터널이 있음
# 맨홀은 터널 위치에 존재

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


types = {
    1: [0, 1, 2, 3], # 상, 우, 하, 좌
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [0, 3]
}


def bfs(R, C):
    queue = [(R, C)]
    visited[R][C] = 1
    cnt = 1
    while queue:
        i, j = queue.pop(0)
        if visited[i][j] == L:
            break
        temp = tunnel[i][j]
        # print(f'tunnel {temp}', f'i: {i}, j:{j}')
        tunnel[i][j] = 0
        for k in types.get(temp):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and tunnel[ni][nj] and (k+2) % 4 in types[tunnel[ni][nj]] and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                cnt += 1
    return cnt


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = bfs(R, C)
    print(f'#{tc} {ans}')
