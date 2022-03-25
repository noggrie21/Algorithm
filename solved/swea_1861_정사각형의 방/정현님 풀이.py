import sys
sys.stdin = open('input (1).txt')

T = int(input())


def make_connect(ts):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i + di[k] < N and 0 <= j + dj[k] < N:
                    if square[i + di[k]][j + dj[k]] == square[i][j] + 1:
                        connect_lst[square[i][j] - 1] = square[i + di[k]][j + dj[k]]
                        break
    print(f'#{ts}', connect_lst)


def find_max():
    max_idx = 0
    max_cnt = 0
    cnt = 1
    for i in range(len(connect_lst) - 1, -1, -1):
        if connect_lst[i]:
            cnt += 1
        else:
            if cnt >= max_cnt:
                max_idx = i + 2
                max_cnt = cnt
            cnt = 1
    if cnt >= max_cnt:
        max_idx = i + 1
        max_cnt = cnt
    return max_idx, max_cnt


for ts in range(T):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    connect_lst = [0] * (N ** 2)
    make_connect(ts)
    # print(connect_lst)
    max_idx, max_cnt = find_max()