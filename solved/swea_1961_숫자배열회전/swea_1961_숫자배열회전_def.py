import sys
sys.stdin = open('input.txt')

T = int(input())

def clockwise(arr):
    result = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            result[c][N-1-r] = arr[r][c]
    return result


for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    arr_90 = clockwise(arr)
    arr_180 = clockwise(arr_90)
    arr_270 = clockwise(arr_180)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), end=' ')
        print(''.join(arr_180[i]), end=' ')
        print(''.join(arr_270[i]))


