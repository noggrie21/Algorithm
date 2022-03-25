import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def Bprint(num):
    ans = ''
    num = int(num, 16)
    for i in range(4):
        ans += '1' if num & (1 << (3-i)) else '0'
    print(ans, end='')


for tc in range(1, T + 1):
    N, num = map(str, input().split())

    print(f'#{tc}', end=' ')
    for i in range(int(N)):
        Bprint(num[i])
    print()

