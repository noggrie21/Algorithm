import sys
sys.stdin = open('sample_input.txt')


def in_order(v):
    global n
    if v <= N:
        in_order(v*2)
        result[v] = n
        n += 1
        in_order(v*2+1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = [0] * (N + 1)
    n = 1
    in_order(1)
    print(f'#{tc} {result[1]} {result[N//2]}')
