import sys
sys.stdin = open('sample_input.txt')

T = int(input())
di = [1, 0]
dj = [0, 1]


def DFS(i, j, total, lst):
    global minV
    if minV < total:
        return

    if i == N - 1 and j == N - 1:
        if total + arr[i][j] < minV:
            minV = total + arr[i][j]
        return

    for k in range(2):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            DFS(ni, nj, total + arr[i][j], lst + [arr[i][j]])


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = (N + N - 1) * 10
    DFS(0, 0, 0, [])
    print(f'#{tc} {minV}')