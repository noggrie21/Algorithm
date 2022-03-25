import sys
sys.stdin = open('input (1).txt')

# 출력 : 처음 출발해야할 방 번호, 최대 몇 개의 방을 이동할 수 있는 지(겹치면 작은 방 번호 뽑기)
# 1 <= A[i][j] <= N**2 (A[i][j]는 모두 다른 수)
# 이동 방향 :  상하좌우
# 이동 조건 : 1. 방이 존재 2. 현재 방 + 1 = 이동하려는 방방


def search(A, N, max_distance, min_num):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not visited[A[i][j]]:
                distance = measure(i, j)
                min_num, max_distance = compare(distance, A[i][j], max_distance, min_num)
    return min_num, max_distance


def measure(i, j):
    cnt = 1
    while True:
        a = A[i][j] + 1
        visited[A[i][j]] = 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if a == A[ni][nj]:
                cnt += 1
                i, j = ni, nj
                break
        else:
            break
    return cnt


def compare(distance, num, max_distance, min_num):
    if max_distance < distance:
        max_distance = distance
        min_num = num
    elif max_distance == distance and num < min_num:
        min_num = num
    return min_num, max_distance


T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    A = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
    visited = [0] * (N**2+1)
    ans = search(A, N, 0, N ** 2)
    print(f'#{tc}', *ans)