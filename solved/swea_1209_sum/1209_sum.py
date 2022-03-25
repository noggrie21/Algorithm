import sys
sys.stdin = open('sum_input (1).txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_total = 0
    totals_cross = [0]*2                 # [대각선 합산, 반대 대각선 합산]
    for i in range(100):
        totals_r_c = [0]*2               # [행 합산, 열 합산]
        totals_cross[0] += arr[i][i]
        totals_cross[1] += arr[i][99-i]
        for j in range(100):
            totals_r_c[0] += arr[i][j]   # 행 합산
            totals_r_c[1] += arr[j][i]   # 열 합산
        for k in range(2):               # 행 합산, 열 합산 중 큰 값으로 max_total 갱신
            if totals_r_c[k] > max_total:
                max_total = totals_r_c[k]
    for l in range(2):
        if totals_cross[l] > max_total:
            max_total = totals_cross[l]
    print(f'#{tc} {max_total}')
