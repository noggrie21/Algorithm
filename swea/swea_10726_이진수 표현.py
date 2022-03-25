import sys
sys.stdin = open('input (1).txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = 'OFF'
    n = 2 ** N - 1
    if (M & n) == n:
        ans = 'ON'
    print(f'#{tc} {ans}')