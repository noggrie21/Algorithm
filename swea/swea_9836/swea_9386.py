import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    i = 0
    cnt = 0
    max_cnt = 0
    while i < N:
        if arr[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
        i += 1
    print(f'#{tc} {max_cnt}')