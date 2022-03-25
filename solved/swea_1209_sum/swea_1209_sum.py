import sys
sys.stdin = open('sum_input (1).txt')

for tc in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0

    # 행 합산
    for i in range(100):
        row_total = 0
        for j in range(100):
            row_total += arr[i][j]
        if max_value < row_total:
            max_value = row_total

    # 열 합산
    for j in range(100):
        col_total = 0
        for i in range(100):
            col_total += arr[i][j]
        if max_value < col_total:
            max_value = col_total

    # 대각선 합산
    cross = 0
    for i in range(100):
        cross += arr[i][i]
    if max_value < cross:
        max_value = cross

    # 반대 대각선 합산
    cross_r = 0
    for i in range(100):
        cross_r += arr[i][99-i]
    if max_value < cross_r:
        max_value = cross_r
    print(f'#{tc} {max_value}')


