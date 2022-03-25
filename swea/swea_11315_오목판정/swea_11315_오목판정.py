import sys
sys.stdin = open('sample_input.txt')


def check(arr, N):
    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):
            x_cnt = xr_cnt = 0
            for k in range(5):
                if arr[i+k][j+k] == 'o':
                    x_cnt += 1
                if arr[i+4-k][j+k] == 'o':
                    xr_cnt += 1
                r_cnt = c_cnt = 0
                for l in range(5):
                    if arr[i + k][j + l] == 'o':
                        r_cnt += 1
                    if arr[j+l][i+k] == 'o':
                        c_cnt += 1
                if r_cnt == 5 or c_cnt == 5:
                    return 'YES'
            if x_cnt == 5 or xr_cnt == 5:
                return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {check(arr, N)}')








