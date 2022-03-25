'''
N: 도시 크기 / M: 하나의 집이 지불하는 비용
출력: 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스영역을 찾고
그때 홈방범 서비스를 제공받는 집들의 수
(정리하면, 손해가 아닐 때 서비스 제공받는 집의 수가 최대가 되는 거 구하기)
K는 마이너스만 아니면 계속 커져도 돼
'''
import sys
sys.stdin = open('sample_input.txt', 'r')
# from pprint import pprint
# sys.stdout = open('test.txt', 'w')

T = int(input())
di = [-1, 0, 1, 0] # 상, 우, 하, 좌
dj = [0, 1, 0, -1]

cost = [0, 1] + [0] * 39
for i in range(2, 41):
    cost[i] = cost[i-1] + 4*(i-1)


def search(cnt):
    global ans
    for i in range(N):
        for j in range(N):
            ans = max(ans, BFS(i, j))
            if ans == cnt:
                return ans
    return ans


def BFS(r, c):
    queue = [(r, c)]
    visited = [[0] * N for _ in range(N)]

    visited[r][c] = 1
    result = cnt = temp = 0
    if house[r][c]:
        cnt += 1

    while queue:
        i, j = queue.pop(0)

        if visited[i][j] != temp:
            temp = visited[i][j]
            if cost[temp] <= cnt * M:
                result = cnt

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if house[ni][nj]:
                    cnt += 1

    return result


def count_house(N):
    cnt = 0
    for lst in house:
        for elem in lst:
            if elem:
                cnt += 1
    return cnt


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    cnt = count_house(N)
    search(cnt)
    print(f'#{tc} {ans}')