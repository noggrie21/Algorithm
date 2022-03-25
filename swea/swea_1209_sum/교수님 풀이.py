import sys
sys.stdin = open('input (1).txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    c1 = c2 = 0 # 대각선

    for i in range(100):
        c1 += arr[i][i]
        c2 += arr[i][99-i]
    max_sum = c1 if c1 > c2 else c2

    for j in range(100):
        rs = cs = 0
        for k in range(100):
            rs += arr[j][k]
            cs += arr[k][j]
        if rs > max_sum:
            max_sum = rs
        if cs > max_sum:
            max_sum = cs

    print(f'#{tc} {max_sum}')

