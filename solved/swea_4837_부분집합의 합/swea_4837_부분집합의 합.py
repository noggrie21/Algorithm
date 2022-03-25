import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    cnt_result = 0
    for i in range(1, 1<<12):
        total = 0
        cnt_N = 0
        for j in range(12):
            if i & (1<<j):
                cnt_N += 1
                total += A[j]
        if total == K and cnt_N == N:
            cnt_result += 1
    print(f'#{tc} {cnt_result}')

