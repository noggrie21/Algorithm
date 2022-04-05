import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque
'''
출발(0, 0)
도착(N-1, N-1)

이동: 상 하 좌 우

기본적으로 1칸에 1 소비
더 높은 곳으로 이동 시 추가 발생



'''


'''
(어제 라강 문제 풀이를 그대로 적용)

기존 BFS는 중복없이 순회
BFS는 중복방문 가능 다만, 기존 비용보다 적게 들 때
(해당 위치에 대한 비용은 visited 배열에 기록)
'''

T = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우


def BFS(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited = [[100*100*1000] * N for _ in range(N)]                                    # visited를 더 적은 비용으로 도착할 수 있을 때마다 방문하는 형태를 위해 큰 수로 초기화
    visited[si][sj] = 0                                                                 # 시작 위치에서 비용은 0

    while queue:
        # deque하기
        i, j = queue.popleft()

        # queue삽입하기
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:                                             # 상, 하, 좌, 우로 이동할 수 있는 경우
                h = arr[ni][nj] - arr[i][j]
                # h: 새로운 칸 높이 - 현재 칸 높이
                # h*bool(h+abs(h)): 높이에 따라 추가되는 요금
                # h가 -2(음수)일 때, bool(-2+abs(-2)) => bool(0) => False = 0 / h*0 = 0
                # h가 2(양수)일 때, bool(2+abs(2)) => bool(4) => True => 1 / h*1 = h

                if visited[i][j] + 1 + h*bool(h+abs(h)) < visited[ni][nj]:              # (ni, nj)에 도달하기 위한 기존 경로 비용(visited[ni][nj]) > 현재 경로에서 도달하는 비용(visited[i][j] + 1 + h*bool(h+abs(h)))일 때,
                    visited[ni][nj] = visited[i][j] + 1 + h*bool(h+abs(h))              # (ni, nj) 비용 갱신
                    queue.append((ni, nj))                                              # queue에 (ni, nj) 다시 삽입

    return visited[N-1][N-1]


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {BFS(0, 0)}')