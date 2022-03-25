import sys
sys.stdin = open('input (1).txt')
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    snail = [[1] * (N + 2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N + 2)]
    i = j = num = 1
    while num < (N * N) + 1:
        snail[i][j] = num
        if snail[i-1][j] and not snail[i][j+1]:
            j += 1
        elif snail[i][j+1] and not snail[i+1][j]:
            i += 1
        elif snail[i+1][j] and not snail[i][j-1]:
            j -= 1
        elif snail[i][j-1] and not snail[i-1][j]:
            i -= 1
        num += 1
    for n in range(1, N + 1):
        print(*snail[n][1:-1])

