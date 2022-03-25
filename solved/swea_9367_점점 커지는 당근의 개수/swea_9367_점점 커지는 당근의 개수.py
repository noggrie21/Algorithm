import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    # print(carrots)
    i = 1
    cnt = 1
    max_cnt = 1
    while i < N:
        if carrots[i] > carrots[i-1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
        i += 1
    print(f'#{tc} {max_cnt}')