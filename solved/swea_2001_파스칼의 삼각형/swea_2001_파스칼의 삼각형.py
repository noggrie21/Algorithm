import sys
sys.stdin = open('input (1).txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * n for n in range(1, N+1)]
    print(f'#{tc}')

    for i in range(N):
        for j in range(0, i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
                continue
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    for sub_arr in arr:
        print(*sub_arr)

