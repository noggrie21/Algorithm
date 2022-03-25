import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            arr_90[c][N-1-r] = arr[r][c]
            arr_180[N-1-r][N-1-c] = arr[r][c]
            arr_270[N-1-c][r] = arr[r][c]

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), end=' ')
        print(''.join(arr_180[i]), end=' ')
        print(''.join(arr_270[i]))

