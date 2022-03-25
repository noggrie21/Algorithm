import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())

    arr = list(map(int, input().split())) + [0]

    cnt = 1
    cnt_last = 1
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            cnt += 1
        else:
            if cnt_last <= cnt:
                cnt_last = cnt
            cnt = 1

    print(f'#{tc+1} {cnt_last}')